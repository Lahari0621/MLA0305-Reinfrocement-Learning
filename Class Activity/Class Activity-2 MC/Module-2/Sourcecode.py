import pandas as pd


df = pd.read_csv("/content/monte_carlo_dataset.csv")

return_rows = []


for episode in df["Episode"].unique():

    episode_data = df[df["Episode"] == episode].copy()

    rewards = episode_data["Reward"].tolist()

    G = 0
    returns = []

    for reward in reversed(rewards):
        G += reward
        returns.insert(0, G)

    episode_data["Return"] = returns
    return_rows.append(episode_data)


returns_df = pd.concat(return_rows)


returns_df.to_csv("/content/monte_carlo_returns.csv", index=False)

print("Returns dataset created successfully!")
print(returns_df.head())


total_episodes = len(episode_rewards)
total_rewards = df["Reward"].sum()
average_reward = df["Reward"].mean()
max_reward = df["Reward"].max()
min_reward = df["Reward"].min()

print("\n========== MODULE 2 SUMMARY ==========")
print("Rewards Collected Successfully")
print("Total Episodes     :", total_episodes)
print("Total Rewards      :", total_rewards)
print("Average Reward     :", round(average_reward, 2))
print("Maximum Reward     :", max_reward)
print("Minimum Reward     :", min_reward)
print("======================================")
import matplotlib.pyplot as plt


reward_state = df.groupby("State")["Reward"].sum()

plt.figure(figsize=(7,5))
plt.bar(reward_state.index, reward_state.values, color="skyblue")

plt.title("Total Reward Collected by State")
plt.xlabel("States")
plt.ylabel("Total Reward")

plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
summary = pd.DataFrame({
    "Parameter":[
        "Module Name",
        "Total Rewards",
        "Maximum Reward",
        "Minimum Reward",
        "Average Reward"
    ],
    "Value":[
        "Collect Rewards",
        df["Reward"].sum(),
        df["Reward"].max(),
        df["Reward"].min(),
        round(df["Reward"].mean(),2)
    ]
})

print("\n========== MODULE 2 SUMMARY TABLE ==========\n")
print(summary.to_string(index=False))
