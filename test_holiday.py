# test holiday methods

import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar
import time
import data_prep as dprep

dr = pd.date_range(start='2023-01-01', end='2023-12-31')
df = pd.DataFrame()
df['Date'] = dr

cal = calendar()
holidays = cal.holidays(start='2022-12-28', end='2024-01-01')

st = time.process_time()
dtest = dprep.holiday_dataframe(df['Date'])
et = time.process_time()
t = et-st
print("Holiday function time of ",t)



print(df)