import pandas as pd

# Data cleaning = the process of fixing/removing:
#                  incomplete, incorrect, or irrelevant data.
#   ~75% of work done with Pandas is data cleaning

df = pd.read_csv("my genshin spreadsheet - Sheet1.csv")
# print(f"CSV file is:\n{df}")

# deleting data
df_deleted = df.drop(columns=["Type"])
print(df_deleted)

# 2. Handle missing data
df_miss = df.dropna(subset=["Weapon_name"])
print(df_miss)
# replacing
df_fill = df.fillna({"Weapon_name": "Something something"})
print(df_fill)

# 3. Fix inconsistent values
df["Weapon"] = df["Weapon"].replace({"Bow": "Teer-kaman"})
print(df)

# 4. Standardize text
df["Name"] = df["Name"].str.lower()
print(df)

# 5. Fix data types
df["Level"] = df["Level"].astype(float)
print(df.to_string())

# 6. Delete duplicates
df = df.drop_duplicates()
print(df)
