import pandas as pd

s
df = pd.read_csv("data/training_data.csv")


df = df.loc[:, ~df.columns.str.contains("^Unnamed")]


diseases = sorted(df["prognosis"].unique())


mapping = {i: disease for i, disease in enumerate(diseases)}


pd.Series(mapping).to_csv("models/disease_mapping.csv")

print("✅ Correct disease mapping saved")
