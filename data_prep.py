# Data Preparation

# Import packages for function
import pandas as pd

def zip_set(list):
    """
    It takes a list of zip codes, and if the zip code is less than 5 digits, it adds a zero to the
    beginning of the zip code
    
    :param list: a list of zip codes
    :return: A list of zip codes with leading zeros.
    """
    ziplist = []
    for i in range(0,len(list)):
        zip = list[i]
        if len(str(zip))<5:
            zip = '0'+str(zip)
        ziplist.append(zip)
    return ziplist

# First function is holiday/seasonality
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar
def holiday_dataframe(dr,sd,ed):
    # Take data set for each unique date and use hash table appraoch instead of checking for each element in the data set

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
    # `hds = cal.holidays(start = sd, end = ed)` is creating a list of holidays between the start date
    # `sd` and end date `ed` using the USFederalHolidayCalendar from the pandas.tseries.holiday
    # package.
    hds = cal.holidays(start = sd, end = ed)
    
    for i in range(0,107):
        sb = str(i)+" before"
        sa = str(i)+" after"
        sb = pd.DataFrame()
        sa = pd.DataFrame()
        sb['true'] = df['Date'].isin(hds-pd.DateOffset(i))
        sa['true'] = df['Date'].isin(hds+pd.DateOffset(i))
        for d in range(0,len(df['Date'])):
            if df.iloc[(d,1)] == "":
                if sb["true"][d] == True:
                   df.iloc[(d,1)] = i
            if df.iloc[(d,2)] == "":
                if sa["true"][d] == True:
                   df.iloc[(d,2)] = i
        print(i)

    
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