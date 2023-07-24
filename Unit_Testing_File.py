# Unit Testing File
# Handling Unit Tests for each method to be used
# Integration Testing will be a seperate file
# Will be using single entry only for this step

# import statements
# assume tensorflow and keras moving forward
import pandas as pd
import unittest
import time

# Select Data File Packages 
import tkinter as tk
from tkinter import filedialog

# Import package for holiday GUI
import easygui



# Creating Unit Test Class

class TestMethods(unittest.TestCase):
    def test_hol(self):
        # Holiday Start/End Test
        # GUI for holiday start/end dates

        hol_start = easygui.enterbox("Start Date for Holiday?")
        hol_end = easygui.enterbox("End Date for Holiday?")

        hol_s_test = "01-01-2023"
        hol_e_test = "12-31-2023"
        self.assertEqual(hol_start,hol_s_test)
        self.assertEqual(hol_end,hol_e_test)

    def test_read(self):
        # Test ensuring CSV is reading correctly
        imp_csv = filedialog.askopenfilename()
        test_data = pd.read_csv(imp_csv)
        cor_data = pd.DataFrame
        self.assertEqual(cor_data,test_data)

unittest.main()

#This Portion is for testing speed of process on small batches

# This is a GUI to select a file.

root = tk.Tk()
file_path = filedialog.askopenfilename()

# GUI for holiday start/end dates

hol_start = easygui.enterbox("Start Date for Holiday?")
hol_end = easygui.enterbox("End Date for Holiday?")

# importing methods from support files
import data_prep as dprep
import weather_gather as wg

st = time.process_time()
test_data = pd.read_csv(file_path)
et = time.process_time()
t = et-st
print("Read function time of ",t)

st = time.process_time()
test_orig = dprep.zip_set(test_data['ORIG'])
et = time.process_time()
t = et-st
print("Zip function time of ",t)

st = time.process_time()
test_dest = dprep.zip_set(test_data['DEST'])
et = time.process_time()
t = et-st
print("Zip function time of ",t)

st = time.process_time()
dtest = dprep.holiday_dataframe(test_data['%Calendar Date'],hol_start,hol_end)
et = time.process_time()
t = et-st
print("Holiday function time of ",t)

# One-hot encoding the load type column.
st = time.process_time()
ltest = dprep.data_onehot(test_data['Load Type'])
et = time.process_time()
t = et-st
print("One hot function time of ",t)

# One-hot encoding the zip codes.
st = time.process_time()
oztest = dprep.data_onehot(test_orig)
et = time.process_time()
t = et-st
print("One hot function time of ",t)

st = time.process_time()
dztest = dprep.data_onehot(test_dest)
et = time.process_time()
t = et-st
print("One hot function time of ",t)

# This is the weather gathering function. It takes the zip code, country, and date and returns the
# weather data for that zip code on that date.
st = time.process_time()
owtest = wg.wg(test_orig,"us",test_data['%Calendar Date'])
et = time.process_time()
t = et-st
print("Weather function time of ",t)

st = time.process_time()
owtest = pd.concat([owtest['tavg'],owtest['tmin'],owtest['tmax'],owtest['prcp'],owtest['snow']],1)
et = time.process_time()
t = et-st
print("Concat function time of ",t)

print("yes")

st = time.process_time()
dwtest = wg.wg(test_dest,"us",test_data['%Calendar Date'])
et = time.process_time()
t = et-st
print("Weather function time of ",t)

st = time.process_time()
dwtest = pd.concat([dwtest['tavg'],dwtest['tmin'],dwtest['tmax'],dwtest['prcp'],dwtest['snow']],1)
et = time.process_time()
t = et-st
print("Concat function time of ",t)

print("yes")

# Concatenating the dataframes into one dataframe for export.
st = time.process_time()
test_result = pd.concat([ltest,owtest,dwtest,oztest,dztest],1)
et = time.process_time()
t = et-st
print("Concat function time of ",t)

# Saving the dataframe to a csv file.
save_path = filedialog.asksaveasfilename(defaultextension=".csv")

