# Data Preparation

# First Step, Holiday Spacing
import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar

def holiday_dataframe(dr):
    # s and f need to be dates writen as strings in form yyyy-mm-dd
    df = pd.DataFrame()
    df['Date'] = pd.to_datetime(dr)
    df['Days Before'] =  ""
    df['Days After'] = ""
    fdf = pd.DataFrame()
    fdf['Date'] = df['Date']

    # get calendar for holidays in question
    cal = calendar()
    hds = cal.holidays(start = '2020-01-01', end = '2022-12-31')
    
    # add column with dates 
    for i in range(0,107):
        df[str(i)+" before"] = df['Date'].isin(hds-pd.DateOffset(i))
        df[str(i)+" after"] = df['Date'].isin(hds+pd.DateOffset(i))
        for d in range(0,len(df['Date'])):
            if df['Days Before'][d] == "":
                if df[str(i)+" before"][d] == True:
                   df['Days Before'][d] = i
            if df['Days After'][d] == "":
                if df[str(i)+" after"][d] == True:
                   df['Days After'][d] = i

    
    fdf['Days Before'] = df['Days Before']
    fdf['Days After'] = df['Days After']

    return fdf

def load_onehot(lt):
    flthe = pd.get_dummies(lt)
    return flthe

def state_onehot(st):
    st_one_list = pd.get_dummies(st)
    return st_one_list