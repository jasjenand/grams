#import libraries & assign csv file
import pandas as pd
import numpy as np
hot100 = pd.read_csv("HotStuff2.csv")

#order csv file by week and chart position
hot100["WeekID"]=pd.to_datetime(hot100["WeekID"])
hot100.sort_values(["WeekID", "Week Position"], inplace=True, ascending=True)

hot100.set_index("WeekID").head(101)
