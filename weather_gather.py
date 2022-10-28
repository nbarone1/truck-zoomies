# API pulling
# Done seperately from data preperation for Readability

import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
from meteostat import Stations, Daily,Point
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

def latlon(zip,country):
    """
    It takes a zip code and a country code as input, and returns the latitude and longitude of the zip
    code
    
    :param zip: the zip code you want to get the latitude and longitude for
    :param country: The country code for the country you want to search in
    :return: A tuple of latitude and longitude
    """
    nomi = pgeocode.Nominatim(country)
    if len(zip)<5:
        zip = '0'+str(zip)
    locdata = nomi.query_postal_code(zip)
    lat,lon = locdata['latitude'],locdata['longitude']
    return lat,lon

def weather_gather(zip,country,date):
    """
    This function takes a zip code, country, and date as inputs and returns the weather data for that
    location on that date
    
    :param zip: The zip code of the location you want to get weather data for
    :param country: The country where the zip code is located
    :param date: The date of the weather data you want to gather
    :return: A dataframe with the following columns:
        station	The Meteostat ID of the weather station (only if query refers to multiple stations)	String
        time	The date	Datetime64
        tavg	The average air temperature in °C	Float64
        tmin	The minimum air temperature in °C	Float64
        tmax	The maximum air temperature in °C	Float64
        prcp	The daily precipitation total in mm	Float64
        snow	The snow depth in mm	Float64
        wdir	The average wind direction in degrees (°)	Float64
        wspd	The average wind speed in km/h	Float64
        wpgt	The peak wind gust in km/h	Float64
        pres	The average sea-level air pressure in hPa	Float64
        tsun    The daily sunshine total in minutes (m)	Float64
    """
    date =pd.to_datetime(date)
    lat,lon = latlon(zip,country)
    point = Point(lat,lon)
    data = Daily(point,date,date)
    data = data.fetch()
    # Converting the temperatures from Celsius to Fahrenheit and the precipitation + snow from millimeters to inches.
    data['tavg']=(data['tavg']*9/5)+32
    data['tmin']=(data['tmin']*9/5)+32
    data['tmax']=(data['tmax']*9/5)+32
    data['prcp']=data['prcp']/25.4
    data['snow']=data['snow']/25.4
    return data

def wg(zips,country,dates):
    """
    This function takes in a list of zip codes, a country, and a list of dates, and returns a dataframe
    of weather data for each zip code
    
    :param zips: list of zip codes
    :param country: 'US' or 'CA'
    :param dates: a list of dates in the format of 'YYYY-MM-DD'
    :return: A dataframe with the weather data for each zip code.
    """
    wg = pd.DataFrame(columns=['time','tavg','tmin','tmax','prcp','snow','wdir','wspd','wpgt','pres','tsun'])
    for i in range(0,len(zips)):
        data = weather_gather(str(zips[i]),country,dates[i])
        wg = pd.concat([wg,data])
    return wg

# A test to see if the weather_gather function works.
# zip = [60640,60630]
# country = 'US'
# date = ["01/01/2022","01/01/2022"]
# data = weather_gather(zip,country,date)
# wg(zip,country,date)
# ds = data.shape

# # print(ds)