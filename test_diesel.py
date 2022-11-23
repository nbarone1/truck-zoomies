# Test Diesel Code

import pandas as pd
import os
from uszipcode import SearchEngine

PATH = os.getcwd()

diesel_data = pd.read_csv(PATH+'\diesel_test_1.csv')

diesel_data['Date'] = pd.to_datetime(diesel_data['Date'],format='%m/%d/%Y')
diesel_data.set_index('Date').resample('D').ffill().reset_index()

zipcodes = [74135,60660,60640,20002]
Date = pd.DataFrame(['3/7/2021','6/22/2022','10/4/2022','10/5/2022'],columns=['Date'])
Date['Date'] = pd.to_datetime(Date['Date'],format='%m/%d/%Y')

def assign_duoarea(lists):
    """
    It takes a list of zip codes and returns the corresponding duoarea
    
    :param lists: a list of zipcodes
    """
    engine = SearchEngine()
    da = []
    duoareas = {'R10X':['CT','ME','MA','NH','RI','VT'], 
            'R10Y':['DE','DC','MD','NJ','NY','PA'],
            'R10Z':['FL','GA','NC','SC','VA','WV'],
            'R20' :['IL','IN','IA','KS','KY','MI','MN','MO','NR','ND','OH','OK','SD','TN','WI'],
            'R30' :['AL','AR','LA','MS','NM','TX'],
            'R40' :['CO','ID','MT','UT','WY'],
            'R5XCA' :['AK','AZ','HA','NV','OR','WA'],
            'SCA':['CA']}
    for i in range(0,len(lists)):
        st = engine.by_zipcode(lists[i])
        kpos = [k for k,v in duoareas.items() if st.state_abbr in v]
        da.append(kpos[0])
    return da
        
DuoArea = pd.DataFrame(assign_duoarea(zipcodes),columns=['DuoArea'])
data = pd.concat([Date,DuoArea],1)

print(diesel_data['Date'])

print(diesel_data.iloc[50])

def pricepull(data,reference):
    pricelist = pd.DataFrame()
    datelist = list(reference['Date'])
    for i in range(0,len(data['Date'])):
        day = data.iloc[i][0]
        day = day.strftime('%Y-%m-%d')
        dayindex = datelist.index(day)
        region = int(reference.columns.get_loc(data.iloc[i][1]))
        print(region)
        price = reference.iloc[dayindex][region]
        pricelist[i] = price
    return pricelist

prices = pricepull(data,diesel_data)