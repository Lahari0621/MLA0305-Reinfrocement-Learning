import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("/content/monte_carlo_dataset.csv")

print("Original Dataset:")
print(df.head())


returns_data = []


for episode in df["Episode"].unique():

    episode_df = df[df["Episode"] == episode].copy()

    rewards = episode_df["Reward"].tolist()

    G = 0
    returns = []
    for reward in reversed(rewards):
        G += reward
        returns.insert(0, G)


    episode_df["Return"] = returns

    returns_data.append(episode_df)


returns_df = pd.concat(returns_data)


returns_df.to_csv("/content/monte_carlo_returns.csv", index=False)

print("\nReturns Dataset (First 10 Records):")
print(returns_df.head(10))

print("\n========== MODULE 3 SUMMARY ==========")
print("Returns Computed Successfully")
print("Total Episodes      :", returns_df["Episode"].nunique())
print("Total Records       :", len(returns_df))
print("Average Return      :", round(returns_df["Return"].mean(),2))
print("Maximum Return      :", returns_df["Return"].max())
print("Minimum Return      :", returns_df["Return"].min())
print("Returns File Saved  : monte_carlo_returns.csv")
print("======================================")


episode_return = returns_df.groupby("Episode")["Return"].mean()

plt.figure(figsize=(10,5))

plt.plot(episode_return.index,
         episode_return.values,
         marker='o',
         color='blue')

plt.title("Average Return per Episode")
plt.xlabel("Episode")
plt.ylabel("Average Return")
plt.grid(True)

plt.show()
summary = pd.DataFrame({
    "Parameter":[
        "Module Name",
        "Output File",
        "Total Records",
        "Average Return",
        "Maximum Return"
    ],
    "Value":[
        "Compute Returns",
        "monte_carlo_returns.csv",
        len(returns_df),
        round(returns_df["Return"].mean(),2),
        returns_df["Return"].max()
    ]
})
print("\n========== MODULE 3 SUMMARY TABLE ==========\n")
print(summary.to_string(index=False))
