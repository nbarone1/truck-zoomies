# MODEL OUTLINE/PSUEDO CODE

# import statements, assuming we go with tensorflow
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


# idea for model - time series with LSTM for certain parameters
# LSTM for price, labor, fuel

# Params right now: historical cost, historical fuel, temp, precipitation, market, seasonality (holiday, harvest season), DAT frequency, maitenance proxy, load type 
# Cost, Market, (DAT), load type - ALX/ALC data
# DAT frequency, line cost, fuel cost - DAT database
# temp, precipitation - visual crossing weather
# seasonality - build calendar
# labor - ??? statista offers a data set adjacent thing
# maitenance statistics - ???
# historical fuel - Collect API (get data by state and city) & EIA API