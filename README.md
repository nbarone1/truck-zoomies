# truck-zoomies
Prediction on Truck Zoomies

 - Attempt to model based on cost factors
 - Focus on historical data including price, weather, etc. etc.
 - Key Indicators coming from people in industry

# Notes on Model
- idea for model - time series with LSTM for certain parameters
- LSTM for price, labor, fuel
- Build some form of Recurrent Nueral Network

- * are done
- Params : historical cost, historical fuel, temp, precipitation, seasonality (holiday), DAT (SnowFlake), Market(one hot)*, load type (one hot)*
- DAT frequency, line cost, fuel cost - DAT database
- cost, load type, market - ALX
- temp, precipitation - weather data coming from meteostat data
- seasonality - calendar in python/pandas
- historical fuel - EIA API and investigating another one (BarChart - waiting for response to inquiry)

- one hot - load type, market
- numericals - miles, cost, dat, dat frequency, line cost, historical fuel, temp, precipitation

- Data prep done in seperate file*, weather gathering in another*, fuel in a third, RNN in a fourth, testing in a fifth
- idea is to keep one file clean as a main*