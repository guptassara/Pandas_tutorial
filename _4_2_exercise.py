import pandas as pd

df = pd.read_csv("my genshin spreadsheet - Sheet1.csv", index_col="Name")
print(f"CSV file is:\n{df}")

character = input("Enter a genshin character name: ")
try:
    print(df.loc[character])
except KeyError:
    print(f"{character} not found")
