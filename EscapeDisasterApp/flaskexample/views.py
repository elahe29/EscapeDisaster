import os
from sklearn.externals import joblib
from settings import APP_STATIC              
from flask import render_template,redirect,request,url_for
from flaskexample import app
import pandas as pd
import numpy as np
import datetime as dt



@app.route('/')
@app.route('/index')
@app.route('/input')
def dropdown():
    #sql_query = """
    #           SELECT distinct "STATE","STATE_FIPS" FROM location_table ORDER BY "STATE";
    #            """
    #query_results=pd.read_sql_query(sql_query,con)
    #states_list = query_results["STATE"].values
    #states = states_list
    #months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    #return render_template('input.html', states=states,months=months)

    dir = os.path.dirname(__file__)
    path_flight = os.path.join(dir, 'flight_df_table.csv')


    flight_df = pd.DataFrame.from_csv(path_flight)
    flight_df_result=flight_df["DEST_CITY_NAME"].drop_duplicates()
    cities_list=flight_df_result.sort_values()
    cities = cities_list

    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    return render_template('input.html', cities=cities,months=months)


def travel_input():
    return render_template("input.html")


#@app.route('/output')
#def wow():
#  date = request.args.get('date')
#  return render_template("output.html",date=date)

@app.route('/output')
def travel_output():

  
  dir = os.path.dirname(__file__)
  path_flight = os.path.join(dir, 'flight_df_table.csv')


  flight_df = pd.DataFrame.from_csv(path_flight)
  flight_df_result=flight_df["DEST_CITY_NAME"].drop_duplicates()
    
  cities_list=flight_df_result.sort_values()
  cities = cities_list

  months = ['January','February','March','April','May','June','July','August','September','October','November','December']

  month_mapping = {
    'January': 1,
    'February': 2,
    'March':3,
    'April':4,
    'May':5,
    'June':6,
    'July':7,
    'August':8,
    'September':9,
    'October':10,
    'November':11,
    'December':12
  }  

  reverse_month_mapping = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
  }  


  date = request.args.get('date')
  cityst = request.args.get('CITY')
  #date = str(date)

  parsed_date = date.split("-")

  year = int(parsed_date[0])
  month = int(parsed_date[1])
  day = int(parsed_date[2])

  #I should have results in the form of st = state_fips and loc in the form of cz_fips and month in the form of
  #name


  
  [city ,state_ab]= cityst.split(',')
  city=city.strip()
  state_ab=state_ab.strip()

  dir = os.path.dirname(__file__)
  path_city = os.path.join(dir, 'city_fips_table.csv')


  city_df = pd.DataFrame.from_csv(path_city)
  city_df_result=city_df[(city_df['STATE_AB'] == state_ab) & (city_df['city'] ==city)]
  fips = city_df_result['fips'].values[0]

  fips = str(np.int(fips))
  st=fips[0:2]
  ### this type casting is to change values like 009 to 9
  loc=str(int(fips[2:5]))



  x_t = np.array([month,float(st),float(loc)])
  x_t =x_t.reshape(1, -1)
  #x_t = [0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,12.0 ,45.0] 
  mod_tornado = joblib.load(os.path.join(APP_STATIC, 'svmodel1_ststyle.pkl'))
  mod_wet = joblib.load(os.path.join(APP_STATIC, 'svmodel2_ststyle.pkl')) 
  mod_cold = joblib.load(os.path.join(APP_STATIC, 'svmodel3_ststyle.pkl'))
  mod_flight = joblib.load(os.path.join(APP_STATIC, 'svmodel4_ststyle.pkl'))  
  predict_tornado=mod_tornado.predict(x_t)
  predict_wet=mod_wet.predict(x_t)
  predict_cold=mod_cold.predict(x_t)

  fipspr = float(fips)
  x_t_flight =np.array([month,fipspr])
  x_t_flight =x_t_flight.reshape(1, -1)
  predict_cancellation=mod_flight.predict(x_t_flight)
  risk_factor = False
  risk_stmt =""
  if predict_tornado == 1:
 
    tornado_result = 'Tornado\n'
    risk_stmt+=tornado_result
    risk_factor = True

  if predict_wet == 1:
    
    wet_result = 'Heavy Rain, Flash Flood, Lightning\n'
    risk_stmt+=wet_result
    risk_factor = True

  if predict_cold == 1:

    cold_result = 'Extreme Cold, Wind Chill, Winter Storm, Blizzard, Heavy Snow\n' 
    risk_stmt+=cold_result
    risk_factor = True

  flight_cancellation = {
  	0:'High',
  	1:'Medium',
  	2:'Low'

  }
 
  if predict_cancellation in [0,1]:
  	  flight_risk =1
  else:
  	  flight_risk = 0




  best_months=''
  bestMonth=0
  for m in range(1,13):
      tornado_r=mod_tornado.predict([[m,float(st),float(loc)]])
      wet_r=mod_wet.predict([[m,float(st),float(loc)]])
      cold_r=mod_cold.predict([[m,float(st),float(loc)]])
      if ((not tornado_r and not wet_r and not cold_r) or (not flight_risk)):
        
        if (not bestMonth):
          best_months += (reverse_month_mapping[m])
          bestMonth=1
        else:
          best_months += (","+reverse_month_mapping[m])
          

        


  return render_template("output.html",selectedDate=date,month_name=reverse_month_mapping[month],day=day,date=date,tornado_risk= predict_tornado, cold_risk = predict_cold, wet_risk= predict_wet,month=month,selectedCity=cityst ,cities=cities,months=months,risk_factor=risk_factor,flight_risk=flight_risk,best_months=best_months,bestMonth=bestMonth)



