# Gather Fuel Data to populate data
# Get Average Fuel Price for that week based around 

# The above code is importing the necessary libraries for the code to run.
import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
import matplotlib.ticker as ticker

# This is the API key that is needed to access the data from the EIA website.
API_KEY = '0JWYgxKIukehAgfhGxGGWgeoARIQhUCyU1JPRke9'
url = 'https://api.eia.gov/v2/petroleum/pri/gnd/data/api_key='+API_KEY
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
                ]
            },
            "start": "2021-01-01",
            "end": None,
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
            "api-version": "2.0.3"
        }

def get_fuel():
    f = requests.get(url,header)
    print(f)
    return

get_fuel()