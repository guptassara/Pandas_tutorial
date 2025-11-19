# DataFrame = A tabular data structure with rows AND columns. (2 Dimensional)
# Similar to an Excel spreadsheet

import pandas as pd

data = {
    "name": [
        "Amber",
        "Diluc",
        "Jean",
        "Klee",
        "Venti",
        "Xiangling",
        "Zhongli",
        "Ganyu",
    ],
    "Age": [20, 22, 20, 10, 2600, 14, 6000, 3000],
}

df = pd.DataFrame(
    data,
    index=pd.Index(
        [
            "Employee 1",
            "Employee 2",
            "Employee 3",
            "Employee 4",
            "Employee 5",
            "Employee 6",
            "Employee 7",
            "Employee 8",
        ],
    ),
)

print(df)
print(df.loc["Employee 3"])
print(df.iloc[1])


# add a new column
df["job"] = [
    "Outrider",
    "Vintner",
    "Acting Grand Master",
    "Spark Knight",
    "Wind Bard",
    "Chef",
    "Geo Archon",
    "Secretary",
]

print(df)

# adding rows
new_row = pd.DataFrame(
    [
        {"name": "Sigewinn", "Age": 400, "job": "Head nurse"},
        {"name": "Clorinde", "Age": 22, "job": "Master Duelist"},
    ],
    index=pd.Index(["Employee 9", "Employee 10"]),
)
df = pd.concat([df, new_row])
print(df)
