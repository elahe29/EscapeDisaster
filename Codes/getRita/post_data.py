POST_DATA="""
UserTableName=On_Time_Performance&DBShortName=&RawDataTable=T_ONTIME&sqlstr=+SELECT+
YEAR,MONTH,DAY_OF_MONTH,FL_DATE,FL_NUM,ORIGIN_AIRPORT_ID,ORIGIN_CITY_MARKET_ID,ORIGIN,
ORIGIN_CITY_NAME,ORIGIN_STATE_ABR,ORIGIN_STATE_FIPS,ORIGIN_STATE_NM,DEST_AIRPORT_ID,
DEST_CITY_MARKET_ID,DEST,DEST_CITY_NAME,DEST_STATE_ABR,DEST_STATE_FIPS,DEST_STATE_NM,
CANCELLED,CANCELLATION_CODE,WEATHER_DELAY

+FROM++T_ONTIME+WHERE+Month+%3D{month}+AND+YEAR%3D{year}&varlist=

YEAR,MONTH,DAY_OF_MONTH,FL_DATE,FL_NUM,ORIGIN_AIRPORT_ID,ORIGIN_CITY_MARKET_ID,ORIGIN,
ORIGIN_CITY_NAME,ORIGIN_STATE_ABR,ORIGIN_STATE_FIPS,ORIGIN_STATE_NM,DEST_AIRPORT_ID,
DEST_CITY_MARKET_ID,DEST,DEST_CITY_NAME,DEST_STATE_ABR,DEST_STATE_FIPS,DEST_STATE_NM,
CANCELLED,CANCELLATION_CODE,WEATHER_DELAY

&grouplist=&suml=&sumRegion=&filter1=title%3D&filter2=title%3D&geo=All%A0&time={month_name}&timename=
Month&GEOGRAPHY=All&XYEAR={year}&FREQUENCY={frequency}&

VarName=YEAR&VarDesc=Year&VarType=Num&
VarName=MONTH&VarDesc=Month&VarType=Num&
VarName=DAY_OF_MONTH&VarDesc=DayofMonth&VarType=Num&
VarName=FL_DATE&VarDesc=FlightDate&VarType=Char&
VarName=FL_NUM&VarDesc=FlightNum&VarType=Char&
VarName=ORIGIN_AIRPORT_ID&VarDesc=OriginAirportID&VarType=Num&
VarName=ORIGIN_CITY_MARKET_ID&VarDesc=OriginCityMarketID&VarType=Num&
VarName=ORIGIN&VarDesc=Origin&VarType=Char&
VarName=ORIGIN_CITY_NAME&VarDesc=OriginCityName&VarType=Char&
VarName=ORIGIN_STATE_ABR&VarDesc=OriginState&VarType=Char&
VarName=ORIGIN_STATE_FIPS&VarDesc=OriginStateFips&VarType=Char&
VarName=ORIGIN_STATE_NM&VarDesc=OriginStateName&VarType=Char&
VarName=DEST_AIRPORT_ID&VarDesc=DestAirportID&VarType=Num&
VarName=DEST_CITY_MARKET_ID&VarDesc=DestCityMarketID&VarType=Num&
VarName=DEST&VarDesc=Dest&VarType=Char&
VarName=DEST_CITY_NAME&VarDesc=DestCityName&VarType=Char&
VarName=DEST_STATE_ABR&VarDesc=DestState&VarType=Char&
VarName=DEST_STATE_FIPS&VarDesc=DestStateFips&VarType=Char&
VarName=DEST_STATE_NM&VarDesc=DestStateName&VarType=Char&
VarName=CANCELLED&VarDesc=Cancelled&VarType=Num&
VarName=CANCELLATION_CODE&VarDesc=CancellationCode&VarType=Char&
VarName=WEATHER_DELAY&VarDesc=WeatherDelay&VarType=Num


"""
