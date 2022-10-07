# test holiday methods

import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar

dr = pd.date_range(start='2015-07-01', end='2015-07-31')
df = pd.DataFrame()
df['Date'] = dr

cal = calendar()
holidays = cal.holidays(start=dr.min(), end=dr.max())

df['2 day before holiday'] = df['Date'].isin(holidays-pd.DateOffset(2))
df['3 day after holiday'] = df['Date'].isin(holidays+pd.DateOffset(3))

print(df)