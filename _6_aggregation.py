# aggregate functions = Reduces a set of values into a single summary value
#                       Used to summarize and analyze data
#                       Often used with the groupby() function

import pandas as pd

df = pd.read_csv("my genshin spreadsheet - Sheet1.csv")
# print(f"CSV file is:\n{df}")

print(f"Mean is\n{df.mean(numeric_only=True)}")
print(f"sum is\n{df.sum(numeric_only=True)}")
print(f"min is\n{df.min(numeric_only=True)}")
print(f"max is\n{df.max(numeric_only=True)}")
print(f"count is\n{df.count()}")

# # single column

print(f"Mean is\n{df["Level"].mean()}")
print(f"sum is\n{df["Talent-attack"].sum()}")
print(f"min is\n{df["Talent-attack"].min()}")
print(f"max is\n{df["Talent-burst"].max()}")
print(f"count is\n{df.count()}")


# group
group = df.groupby("Element")
print(f"Mean of group is:\n{group['Level'].mean()}")
print(f"Min of group is:\n{group['Level'].min()}")
print(f"Max of group is:\n{group['Level'].max()}")
print(f"sum of group is:\n{group['Level'].sum()}")
print(f"count of group is:\n{group['Level'].count()}")
