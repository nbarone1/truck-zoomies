# API pulling
# Done seperately from data preperation for Readability

import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
from meteostat import Stations, Daily
from datetime import datetime
import pgeocode


# Idea is to use Visual Crossing
# decision on weather API determines following imports, API Keys, etc

# import urllib.error
# import urllib.request

# BaseUrlW = ''

# API_KEYW = ''

# start = datetime(2022,1,1)
# end = datetime(2022,10,27)

# data = Daily('10637',start,end)
# data =data.fetch()

# data['tavg']=(data['tavg']*9/5)+32
# data['prcp']=data['prcp']/25.4

# fig,ax1 = plt.subplot()

# ax2 = ax1.twinx()
# ax1.plot(data['tavg'])
# ax2.plot(data['prcp'])

# plt.show()

def weather_gather(Org,Dst):
    
    return Org,Dst