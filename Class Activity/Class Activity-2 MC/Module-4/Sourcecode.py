import pandas as pd
import matplotlib.pyplot as plt


returns_df = pd.read_csv("/content/monte_carlo_returns.csv")

state_values = returns_df.groupby("State")["Return"].mean().reset_index()

state_values.rename(columns={"Return":"State_Value"}, inplace=True)

print(state_values)


state_values.to_csv("/content/monte_carlo_state_values.csv", index=False)

print("\n========== MODULE 4 SUMMARY ==========")
print("State Values Updated Successfully")
print("Total States :", len(state_values))
print("Highest Value:", round(state_values["State_Value"].max(),2))
print("Lowest Value :", round(state_values["State_Value"].min(),2))
print("Average Value:", round(state_values["State_Value"].mean(),2))
print("======================================")

plt.figure(figsize=(8,5))
plt.bar(state_values["State"], state_values["State_Value"], color="lightgreen")
plt.title("Estimated State Values")
plt.xlabel("State")
plt.ylabel("State Value")
plt.grid(axis='y')
plt.show()
state_values = returns_df.groupby("State")["Return"].mean().reset_index()

state_values.rename(columns={"Return":"State_Value"}, inplace=True)

summary = pd.DataFrame({
    "Parameter":[
        "Module Name",
        "Output File",
        "Total States",
        "Highest State Value",
        "Lowest State Value"
    ],
    "Value":[
        "Update State Values",
        "monte_carlo_state_values.csv",
        len(state_values),
        round(state_values["State_Value"].max(),2),
        round(state_values["State_Value"].min(),2)
    ]
})
print("\n========== MODULE 4 SUMMARY TABLE ==========\n")
print(summary.to_string(index=False))
