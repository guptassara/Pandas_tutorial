import pandas as pd

df_csv = pd.read_csv("my genshin spreadsheet - Sheet1.csv")
print(f"CSV file is:\n\n{df_csv.to_string}")
df_json = pd.read_json("my-genshin-spreadsheet-Sheet1.json")
print(f"JSON file is:\n\n{df_json.to_string}")
