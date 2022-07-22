from faker import Faker
from datetime import datetime
from random import randint
import pandas as pd

def time_value_generator_2(file_name, line_num):
    fake = Faker()
    num = [randint(0, 100) for i in range(line_num)]
    time_list = []

    for i in range(line_num):
        times = fake.date_time_between(start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31))
    #   fake.date_time_this_year(before_now=True))
        time_list.append(times)

    df = pd.DataFrame({"Time": time_list, "Value": num})
    df["Time"] = df["Time"].astype("datetime64[ns]")
    df.to_csv(file_name, mode="w", index=False)
    return df

time_value_generator_2(file_name="time_value_2.csv", line_num=100)