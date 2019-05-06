#import libraries & assign csv files
import pandas as pd
import numpy as np

hot100 = pd.read_csv("HotStuff2.csv")
pfork = pd.read_csv("newps4k.csv")
goat = pd.read_csv("goats.csv").set_index("Number")

#order hot100.csv file by week and chart position
hot100["WeekID"]=pd.to_datetime(hot100["WeekID"])
hot100.sort_values(["WeekID", "Week Position"], inplace=True, ascending=True)

hot100.set_index("WeekID").head(101)
pfork.head(30)
goat.head(20)

