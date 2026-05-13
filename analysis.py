import pandas as pd

df = pd.read_csv("predictions.csv")

counts = df["predicted_label"].value_counts()

print(counts)
print("mean:", df["predicted_probability"].mean())
print("median:", df["predicted_probability"].median())
print(">0.9:", (df["predicted_probability"] > 0.9).mean())
print("<0.6:", (df["predicted_probability"] < 0.6).mean())