# MODEL OUTLINE/PSUEDO CODE

# idea for model - time series with LSTM for certain parameters
# LSTM for price, labor, fuel

# import statements, assuming we go with tensorflow
# if possible get access to use tf/keras
import pandas as pd
# import numpy

# importing methods from support files
import data_prep as dprep

# Params right now: historical cost, historical fuel, temp, precipitation, market, seasonality (holiday, harvest season), DAT frequency, maitenance proxy, load type (hot encoded)
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

# Build some form of Recurrent Nueral Network
# Look to if encoding is necessary

# Data prep - ensure we have either names or numbers (do we need to turn O_STATE,D_STATE into a number)
# Data prep done in seperate file, idea is to keep this one clean, act as a main

data = dprep.holiday_dataframe('2022-01-01','2022-10-07')

data.to_csv('file_name.csv',index=False)

loads = ['DRY VAN','REFRIGERATED','DRY LTL','FLATBED']
loads = pd.DataFrame(loads, columns=['Load Type'])

load_specs = dprep.load_onehot(loads)
loads['R'] = load_specs['R']
loads['F'] = load_specs['F']
loads['L'] = load_specs['L']

loads.to_csv('file_name2.csv',index=False)