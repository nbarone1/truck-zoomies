# MODEL OUTLINE/PSUEDO CODE

# idea for model - time series with LSTM for certain parameters
# LSTM for price, labor, fuel

# import statements, assuming we go with tensorflow
import datetime
import requests
import http.client
import tensorflow as tf
import time as t
import numpy as np
import matplotlib.pyplot as plt
import sklearn.model_selection as skl
import pandas as pd
import collections
import math
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize

# Params right now: historical cost, historical fuel, temp, precipitation, market, seasonality (holiday, harvest season), DAT frequency, maitenance proxy, load type 
# Cost, Market, (DAT), load type - ALX/ALC data
# DAT frequency, line cost, fuel cost - DAT database
# temp, precipitation - visual crossing weather
# seasonality - build calendar
# labor - ??? statista offers a data set adjacent thing: Is this something I can get from non data set?
# maitenance statistics - ??? take 16% of variable roughly: non data set information?
# historical fuel - Collect API (get data by state and city) & EIA API
# Does shipper matter?
# Do we want this lande by lane?
#       Otherwise we need fuel/miles for load length
#       Build model lane by lane? can save parameters in a JSON file for future use/development/fine tuned

# onehot encode load, would have to onehot lanes (would likely have to do O_STATE, D_STATE)
# holidays are days after and days before
# numericals - miles, cost, dat, dat frequency, line cost, historical fuel, temp, precipitation, labor, maitenance