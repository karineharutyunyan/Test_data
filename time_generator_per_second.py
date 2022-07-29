"""
The code is infinite Recursive function for creating current datetime and random number and adding these values in csv file.
The datetime value changes by second.
"""
from datetime import datetime
import time
from random import randint
import pandas as pd
import sys


def time_value_generator_to_csv(datarate=1):
#    sys.setrecursionlimit()                                                   # Recursion limit(int)

    while True:
        num_value = pd.Series(randint(0, 100))                                 # Second column with random number
        date_time = pd.Series(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))    # Current datetime
        df = pd.DataFrame({"Time": start_date_time, "Value": num_value})       # Pandas Dataframe creation
        df["Time"] = df["Time"].astype("datetime64[ns]")                       # Change datetime type to datetime64
        df.to_csv("date_time_generator.csv", mode="a", index=False, header=False)  # Writting existing dataframe line to csv file
        time.sleep(datarate)                                                   # Stop script work for a second
        return time_value_generator_to_csv()                                   # Recursion

