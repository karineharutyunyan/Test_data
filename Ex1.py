from random import randint, choice
import pandas as pd


def time_value_generator(file_name, line_num):
    num = [randint(0, 100) for i in range(line_num)]
    time_list = []

    for _ in range(line_num):
        hour = choice(range(24))
        minsec = choice(range(60))
        year = choice(range(2020, 2022))
        month = choice(range(1, 13))
        m_31 = [1, 3, 5, 7, 8, 10, 12]
        m_28_29 = 2
        if month in m_31:
            day = choice(range(1, 31))
        elif month == m_28_29:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                day = choice(range(1, 29))
            else:
                day = choice(range(1, 28))
        else:
            day = choice(range(1, 30))

        times = f"{year}, {month}, {day} {hour}:{minsec}:{minsec}"
        time_list.append(times)

    df = pd.DataFrame({"Time": time_list, "Value": num})
    df["Time"] = df["Time"].astype("datetime64[ns]")
    df.to_csv(file_name, mode="w", index=False)
    return df


time_value_generator(file_name="time_value.csv", line_num=100)