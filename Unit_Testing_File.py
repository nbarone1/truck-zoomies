# Unit Testing File
# Handling Unit Tests for each method to be used
# Integration Testing will be a seperate file
# Will be using single entry only for this step

# import statements
# assume tensorflow and keras moving forward
import pandas as pd
import os
import time

# Select Data File
import tkinter as tk
from tkinter import filedialog

# This is a GUI to select a file.
root = tk.Tk()

file_path = filedialog.askopenfilename()

# Unit Test import
import unittest as ut

# importing methods from support files
import data_prep as dprep
import weather_gather as wg

# This is a timing function to see how long it takes to read in the data.
st = time.process_time()
test_data = pd.read_csv(file_path)
et = time.process_time()
t = et-st
print("Read function time of ",t)

