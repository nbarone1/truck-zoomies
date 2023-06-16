# test holiday methods

import pandas as pd
import time
import data_prep as dprep

dr = pd.date_range(start='2023-01-01', end='2023-12-31')
df = pd.DataFrame()
df['Date'] = dr

start= '2022-12-28'
end='2024-01-01'

st = time.process_time()
dtest = dprep.holiday_dataframe(df['Date'], start, end)
print(dtest)
et = time.process_time()
t = et-st
print("Holiday function time of ",t)

