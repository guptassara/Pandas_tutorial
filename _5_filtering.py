import pandas as pd

df = pd.read_csv("my genshin spreadsheet - Sheet1.csv", index_col="Name")
# print(f"CSV file is:\n{df}")

leveled_characters = df[df["Level"] >= 70]

print(f"Levelled characters are:\n{leveled_characters}")

talented_characters = df[df["Talent-attack"] >= 6]
print(f"Talented characters are:\n{talented_characters}")

constellation = df[df["Constellation"] >= 5]
print(f"Constellation characters are:\n{constellation}")

pyro_character = df[df["Element"] == "pyro"]
print(f"Pyro characters are:\n{pyro_character}")

pyro_character_or_bow = df[(df["Element"] == "pyro") | (df["Weapon"] == "Bow")]
print(f"Pyro or bow characters are:\n{pyro_character_or_bow}")

hydro_caymore_character = df[(df["Element"] == "hydro") & (df["Weapon"] == "Claymore")]
print(f"Hydro claymore characters are:\n{hydro_caymore_character}")
