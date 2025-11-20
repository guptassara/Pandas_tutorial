import pandas as pd

df = pd.read_csv("my genshin spreadsheet - Sheet1.csv", index_col="Name")
print(f"CSV file is:\n{df}")

# selection by column
print(df.index)
print(df[["Level"]])
print(df[["Level", "Weapon"]].to_string())

# selection by row
# print(df.loc[10])
print(df.loc[("Mavuika").lower()])
print(df.loc[("Nefer"), ["Weapon", "Constellation"]])
print(df.loc["mavuika":"clorinde"])
print(df.loc["mavuika":"clorinde", ["Weapon"]])

print(df.iloc[0:11])
print(df.iloc[0:11:2])
print(df.iloc[0:11:2, 0:3])

