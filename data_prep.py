# Data Preparation

# Import packages for function
import pandas as pd

def zip_set(list):
    for i in range(0,len(list)):
        zip = list[i]
        if len(zip)<5:
            zip = '0'+str(zip)
            list[i] = zip
    return list

# First function is holiday/seasonality
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar
def holiday_dataframe(dr):
    """
    It takes a date range and returns a dataframe with the dates in the range and the number of days
    before and after each date that a holiday falls
    
    :param dr: date range
    :return: A dataframe with the dates in the range and the number of days before and after a holiday.
    """
    # s and f need to be dates writen as strings in form yyyy-mm-dd
    df = pd.DataFrame()
    df['Date'] = pd.to_datetime(dr)
    df['Days Before'] =  ""
    df['Days After'] = ""
    fdf = pd.DataFrame()
    fdf['Date'] = df['Date']

    # get calendar for holidays in question
    cal = calendar()
    hds = cal.holidays(start = '2020-01-01', end = '2023-01-01')
    
    # add column with dates 
    # optimize using loc
    # look at frame.insert versus a copy to improve performance
    # PerformanceWarning: DataFrame is highly fragmented.  This is usually the result of calling `frame.insert` many times, which has poor performance.  
    # Consider joining all columns at once using pd.concat(axis=1) instead. To get a de-fragmented frame, use `newframe = frame.copy()`
    for i in range(0,107):
        df.loc[str(i)+" before"] = df['Date'].isin(hds-pd.DateOffset(i))
        df.loc[str(i)+" after"] = df['Date'].isin(hds+pd.DateOffset(i))
        for d in range(0,len(df['Date'])):
            if df.iloc[(1,d)] == "":
                if df[str(i)+" before"][d] == True:
                   df.iloc[(1,d)] = i
            if df.iloc[(2,d)] == "":
                if df[str(i)+" after"][d] == True:
                   df.iloc[(2,d)] = i

    
    fdf['Days Before'] = df['Days Before']
    fdf['Days After'] = df['Days After']

    return fdf


# Second function is one hot encoding
def data_onehot(list):
    """
    It takes a list of categorical values and returns a one-hot encoded dataframe
    
    :param list: the list of data you want to one-hot encode
    :return: A dataframe with the one-hot encoded values.
    """
    ohe = pd.get_dummies(list)
    return ohe