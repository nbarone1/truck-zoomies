# MODEL OUTLINE/PSUEDO CODE

# idea for model - time series with LSTM for certain parameters
# LSTM for price, labor, fuel

# import statements, assuming we go with tensorflow
# if possible get access to use tf/keras
import pandas as pd
import os

PATH = os.getcwd()
# import numpy

# importing methods from support files
import data_prep as dprep
import weather_gather as wg

# * are done
# most APIs have limits, may need to purchase some data connections
# Params right now: historical cost, historical fuel, temp, precipitation, market, seasonality (holiday, harvest season), DAT frequency, maitenance proxy, load type (hot encoded)* 
# Cost, Market, (DAT), load type - ALX/ALC data
# DAT frequency, line cost, fuel cost - DAT database
# temp, precipitation - openweathermap - testing with open metro beginning. looking into downloading data sets instead of using an API - visual crossing may still be useful
# seasonality - build calendar*
# labor - ??? statista offers a data set adjacent thing: Is this something I can get from non data set?
# maitenance statistics - ??? take 16% of variable roughly: non data set information?
# historical fuel - EIA API and investigating another one (BarChart - waiting for response to inquiry), 

# is statista a realistic option
# other free avenues
# do we download bulk data and update manually when we train a model

# holidays are days after and days before*
# numericals - miles, cost, dat, dat frequency, line cost, historical fuel, temp, precipitation, labor, maitenance

# Build some form of Recurrent Nueral Network

# Data prep - ensure we have either names or numbers (do we need to turn O_STATE,D_STATE into a number)*
# Data prep done in seperate file, idea is to keep this one clean, act as a main*
# look ups will be done in seperate file from data_prep

test_data = pd.read_csv(PATH+'\\test_data.csv')
# test_data['ALX_MILES'] = test_data['ALX_MILES'].astype(int)
# test_data['DAT.MOVES'] = test_data['DAT.MOVES'].astype(int)
# test_data['DAT.CONTRIBUTOR_COUNT'] = test_data['DAT.CONTRIBUTOR_COUNT'].astype(int)

dtest = dprep.holiday_dataframe(test_data['%Calendar Date'])

ltest = dprep.load_onehot(test_data['Load Type'])

oztest = dprep.place_onehot(test_data['ORIG'])
dztest = dprep.place_onehot(test_data['DEST'])

owtest = wg.weather_gather(test_data['ORIG'])
owtest = pd.concat([owtest['tavg'],owtest['tmin'],owtest['tmax'],owtest['prcp'],owtest['snow']])

dwtest = wg.weather_gather(test_data['DEST'])
dwtest = pd.concat([dwtest['tavg'],dwtest['tmin'],dwtest['tmax'],dwtest['prcp'],dwtest['snow']])


test_result = pd.concat([dtest,ltest,owtest,dwtest,oztest,dztest])

test_result.to_csv('zip_test_results.csv',index=False)