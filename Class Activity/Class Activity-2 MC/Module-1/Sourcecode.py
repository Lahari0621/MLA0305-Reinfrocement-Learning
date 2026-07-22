import pandas as pd


df = pd.read_csv(r"/content/monte_carlo_dataset.csv")

print(df.head())

print("\n========== MODULE 1 SUMMARY ==========")
print("Dataset Loaded Successfully")
print("Total Records :", len(df))
print("Total Episodes :", df['Episode'].nunique())
print("Total States :", df['State'].nunique())
print("States :", list(df['State'].unique()))
print("======================================")
import matplotlib.pyplot as plt

reward_sum = df.groupby("State")["Reward"].sum()

plt.figure(figsize=(7,5))
plt.bar(reward_sum.index, reward_sum.values)

plt.title("Reward Distribution by State")
plt.xlabel("State")
plt.ylabel("Total Reward")

plt.show()
