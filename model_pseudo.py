# MODEL OUTLINE/PSUEDO CODE

# import statements, assuming we go with tensorflow
import requests
import tensorflow as tf


# idea for model - time series with LSTM for certain parameters
# LSTM for price, labor, fuel

# Params right now: historical cost, historical fuel, temp, precipitation, market, seasonality (holiday, harvest season), DAT frequency, maitenance proxy, load type 
# Cost, Market, (DAT), load type - ALX/ALC data
# DAT - DAT database
# temp, precipitation - visual crossing weather
# seasonality - build calendar
# maitenance statistics - ???