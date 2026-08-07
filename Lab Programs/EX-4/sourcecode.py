import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

arms = 5
iterations = 1000
epsilon = 0.1

true_rewards = [0.2, 0.5, 0.75, 0.6, 0.35]

Q = np.zeros(arms)
N = np.zeros(arms)

total_reward = 0
cumulative_reward = []

exploration = 0
exploitation = 0

exploration_history = []
exploitation_history = []

for i in range(iterations):

    if np.random.rand() < epsilon:
        action = np.random.randint(arms)
        exploration += 1
    else:
        action = np.argmax(Q)
        exploitation += 1

    reward = 1 if np.random.rand() < true_rewards[action] else 0

    N[action] += 1
    Q[action] += (reward - Q[action]) / N[action]

    total_reward += reward
    cumulative_reward.append(total_reward)

    exploration_history.append(exploration)
    exploitation_history.append(exploitation)

print("========== SUMMARY ==========")
print("Algorithm :", "Epsilon-Greedy Multi-Armed Bandit")
print("Number of Arms :", arms)
print("Iterations :", iterations)
print("Exploration Rate (ε) :", epsilon)

print("\n========== RESULT ==========")

print("\nEstimated Rewards")
for i in range(arms):
    print("Arm", i + 1, ":", round(Q[i], 3))

print("\nAction Selection Count")
for i in range(arms):
    print("Arm", i + 1, ":", int(N[i]))

print("\nExploration Steps :", exploration)
print("Exploitation Steps :", exploitation)

print("\nTotal Reward :", total_reward)

plt.figure(figsize=(8,5))
plt.plot(cumulative_reward)
plt.title("Cumulative Reward vs Iterations")
plt.xlabel("Iterations")
plt.ylabel("Cumulative Reward")
plt.grid(True)

plt.figure(figsize=(8,5))
plt.plot(exploration_history, label="Exploration")
plt.plot(exploitation_history, label="Exploitation")
plt.title("Exploration vs Exploitation")
plt.xlabel("Iterations")
plt.ylabel("Number of Selections")
plt.legend()
plt.grid(True)

plt.figure(figsize=(6,5))
plt.bar(range(1, arms + 1), N)
plt.title("Action Selection Frequency")
plt.xlabel("Bandit Arms")
plt.ylabel("Selections")
plt.xticks(range(1, arms + 1))
plt.grid(axis="y")

plt.show()
