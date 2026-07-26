import pandas as pd
import matplotlib.pyplot as plt


returns_df = pd.read_csv("/content/monte_carlo_returns.csv")

print("Monte Carlo Simulation Started...\n")

history = []

episodes = sorted(returns_df["Episode"].unique())


for episode in episodes:

    current_data = returns_df[returns_df["Episode"] <= episode]


    state_values = current_data.groupby("State")["Return"].mean()

    history.append([
        state_values.get("A", 0),
        state_values.get("B", 0),
        state_values.get("C", 0),
        state_values.get("D", 0),
        state_values.get("Terminal", 0)
    ])

print("Simulation Completed Successfully!\n")


final_values = pd.DataFrame({
    "State": ["A", "B", "C", "D", "Terminal"],
    "Final_State_Value": history[-1]
})

print("Final Estimated State Values:\n")
print(final_values)


final_values.to_csv("/content/final_state_values.csv", index=False)

print("\n========== MODULE 5 SUMMARY ==========")
print("Simulation Completed Successfully")
print("Episodes Processed :", len(episodes))
print("Total Records      :", len(returns_df))
print("Output File        : final_state_values.csv")
print("Monte Carlo Process Repeated Successfully")
print("======================================")


history_df = pd.DataFrame(
    history,
    columns=["A", "B", "C", "D", "Terminal"]
)


plt.figure(figsize=(10,6))

plt.plot(history_df["A"], label="State A")
plt.plot(history_df["B"], label="State B")
plt.plot(history_df["C"], label="State C")
plt.plot(history_df["D"], label="State D")
plt.plot(history_df["Terminal"], label="Terminal")

plt.title("Monte Carlo State Value Convergence")
plt.xlabel("Episode")
plt.ylabel("Estimated State Value")
plt.legend()
plt.grid(True)

plt.show()
summary = pd.DataFrame({
    "Parameter":[
        "Module Name",
        "Simulation",
        "Episodes Processed",
        "Output File",
        "Status"
    ],
    "Value":[
        "Repeat Process",
        "Monte Carlo",
        len(episodes),
        "final_state_values.csv",
        "Completed"
    ]
})
print("\n========== MODULE 5 SUMMARY TABLE ==========\n")
print(summary.to_string(index=False))
