# test holiday methods

import pandas as pd
import time
import data_prep as dprep
import easygui

dr = pd.date_range(start='2023-01-01', end='2023-12-31')
df = pd.DataFrame()
df['Date'] = dr

start = easygui.enterbox("Start Date for Holiday?")
end = easygui.enterbox("End Date for Holiday?")

st = time.process_time()
dtest = dprep.holiday_dataframe(df['Date'], start, end)
print(dtest)
et = time.process_time()
t = et-st
print("Holiday function time of ",t)

