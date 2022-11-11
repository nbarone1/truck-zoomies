# Test Diesel Code

import pandas as pd
import os
from uszipcode import SearchEngine

PATH = os.getcwd()

diesel_data = pd.read_csv(PATH+'\diesel_test_1.csv')

diesel_data['Date'] = pd.to_datetime(diesel_data['Date'])
diesel_data.set_index('Date').resample('D').ffill().reset_index()

print(diesel_data)

lists = [74135,60660,60640,20002]

def assign_duoarea(lists):
    """
    It takes a list of zip codes and returns the corresponding duoarea
    
    :param lists: a list of zipcodes
    """
    engine = SearchEngine()
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
        print(kpos[0])
        
assign_duoarea(lists)