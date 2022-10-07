# Data Preparation

# First Step, Holiday Spacing

import datetime
import time as t
import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar

def holiday_dataframe(s,f):
    # s and f need to be dates writen as strings in form yyyy-mm-dd
    dr = pd.date_range(start=s,end=f)
    df = pd.DataFrame()
    df['Date'] = dr

    # get calendar for holidays in question
    cal = calendar()
    hds = cal.holidays(start = dr.min, end = dr.max())

    d = 0
    for d in range(0,len(df)):
        b = 0
        a = 0
        while not(df['Date'[d]].isin(hds-pd.DateOffset(b))):
            b = b+1
        while not(df['Date'[d]].isin(hds+pd.DateOffset(a))):
            a = a+1
        df['Days Before'[d]]=b
        df['Days After'[d]]=a
    
    return df
    
