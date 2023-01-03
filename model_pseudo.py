# MODEL OUTLINE/PSUEDO CODE

# import statements, assuming we go with tensorflow and keras moving forward
import pandas as pd
import os

# Set Path
PATH = os.getcwd()

# importing methods from support files
import data_prep as dprep
import weather_gather as wg


test_data = pd.read_csv(PATH+'\zipcode_test.csv')

test_orig = dprep.zip_set(test_data['ORIG'])
test_dest = dprep.zip_set(test_data['DEST'])

dtest = dprep.holiday_dataframe(test_data['%Calendar Date'])

# One-hot encoding the load type column.
ltest = dprep.data_onehot(test_data['Load Type'])

# One-hot encoding the zip codes.
oztest = dprep.data_onehot(test_orig)
dztest = dprep.data_onehot(test_dest)

# This is the weather gathering function. It takes the zip code, country, and date and returns the
# weather data for that zip code on that date.
owtest = wg.wg(test_orig,"us",test_data['%Calendar Date'])
owtest = pd.concat([owtest['tavg'],owtest['tmin'],owtest['tmax'],owtest['prcp'],owtest['snow']],1)
print("yes")
dwtest = wg.wg(test_dest,"us",test_data['%Calendar Date'])
dwtest = pd.concat([dwtest['tavg'],dwtest['tmin'],dwtest['tmax'],dwtest['prcp'],dwtest['snow']],1)
print("yes")

# Concatenating the dataframes into one dataframe for export.
test_result = pd.concat([ltest,owtest,dwtest,oztest,dztest],1)

# Saving the dataframe to a csv file.
test_result.to_csv('zip_test_results.csv',index=False)