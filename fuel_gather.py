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
API_KEY = '0JWYgxKlukehAgfhGxGGWgeoARIQhUCyU1JPRke9'
url = 'https://api.eia.gov/v2/petroleum/pri/gnd/data/?api_key'+API_KEY