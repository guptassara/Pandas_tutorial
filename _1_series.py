# Series = A Pandas 1dimensional labeled array that can hold any data type. Think of it like a single column in a spreadsheet (1- Dimensional)

import pandas as pd

data = [100, 102, 104, 200, 202]
series = pd.Series(data)  # Series is a constructor not function
print(series)

data2 = [100.90, 102.4, 104.33]
series = pd.Series(data2)  # Series is a constructor not function
print(series)

data3 = ["A", "B", "C"]
series = pd.Series(data3)  # Series is a constructor not function
print(series)

data4 = [True, False, True]
series = pd.Series(data4)  # Series is a constructor not function
print(series)

data5 = [True, False, True, "abc", 120.90, 19]
series = pd.Series(data5)  # Series is a constructor not function
print(series)

series = pd.Series(
    data,
    index=[
        "apartment #1",
        "apartment #2",
        "apartment #3",
        "apartment #4",
        "apartment #5",
    ],
)
print(series)

series = pd.Series(data, index=["a", "b", "c", "d", "e"])
print(series)

# loc loaction by label
print(series.loc["a"])
series.loc["b"] = 20000
print(series)

print(series.iloc[1])  # integer location

print(series[series >= 200])
print(series[series < 200])


# dictionary

calories = {"Day 1": 1750, "Day 2": 1900, "Day 3": 2200, "Day 4": 1500, "Day 5": 1230}
series_calorie = pd.Series(calories)
print(series_calorie)
print(series_calorie.loc["Day 3"])
series_calorie.loc["Day 2"] += 500
print(series_calorie)
print(series_calorie[series_calorie >= 2000])
print(series_calorie[series_calorie < 2000])
