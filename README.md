# EscapeDisaster
EscapeDisaster.live is a predictive website to anticipate flights cancellation/delays due to severe weather conditions and help travelers to choose the best time to visit a city.
The app is created by:
- Scraping NOAA weather API data and USA department of transportation API data using Python, Pandas, PostgreSQL
- Training multiple Non-Linear SVM classifiers one for each natural event and flight cancelation. Integrated these classifiers to perform my prediction using numpy, scikit-learn in Python and flask, bootstrap, AWS for the web interface.

### To get the data:
you can use the code in EscapeDisaster/Codes/getRita to get flight information Data and use EscapeDisaster/Codes/NOAA_SWD_BULK.py to get NOAA severe weather data

### To Build SQL Dataset:
The code is located at EscapeDisaster/Codes/SetupSQL.ipynb

### To Clean NOAA data and build natural events classifiers:
The code is located at EscapeDisaster/Codes/NaturalDisasters.ipynb

### To Clean Flight Information data and build flight Cancellation/Delay classifier:
The code is located at EscapeDisaster/Codes/FlightCancellation.ipynb
