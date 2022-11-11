# Gather Fuel Data to populate data
# Get Average Fuel Price for that week based around 

# The above code is importing the necessary libraries for the code to run.
import pandas as pd
import requests
from uszipcode import SearchEngine
from datetime import date
# import os


# This is the API key that is needed to access the data from the EIA website.
API_KEY = '0JWYgxKIukehAgfhGxGGWgeoARIQhUCyU1JPRke9'
url = 'https://api.eia.gov/v2/petroleum/pri/gnd/data/api_key='+API_KEY+"&facets[product][]=EPD2D"
print(url)

# A dictionary that is used to pass parameters to the API.
header = {
            "frequency": "weekly",
            "data": [
                "value"
            ],
            "facets": {
                "product": [
                    "EPD2D"
                ],
                "duoarea": [
                    "R1X",
                    "R1Y",
                    "R1Z",
                    "R20",
                    "R30",
                    "R40",
                    "R5XCA",
                    "SCA"
                ]
            },
            "start": "2021-01-01",
            "end": "null",
            "sort": [
                {
                    "column": "period",
                    "direction": "desc"
                },
                {
                    "column": "duoarea",
                    "direction": "asc"
                }
            ],
            "offset": 0,
            "length": 5000,
            "api-version": "2.0.4"
        }

def get_fuel():
    f = requests.get(url)
    print(f)
    return

def get_key(my_dict,val):
    """
    It takes a dictionary and a value, and returns the key that corresponds to that value
    
    :param my_dict: the dictionary you want to search
    :param val: the value you're looking for
    :return: The key of the dictionary
    """
    for key, value in my_dict.items():
        if val == value:
            return key

get_fuel()

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