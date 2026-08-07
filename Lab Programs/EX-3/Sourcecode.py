import numpy as np
import matplotlib.pyplot as plt

gamma = 0.9

states = ["S0", "S1", "S2", "Goal"]

rewards = np.array([-1, -2, 10, 0])

P = np.array([
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1],
    [0,0,0,1]
])

V = np.zeros(4)

iterations = []
history = []

for i in range(15):
    new_V = np.zeros(4)
    for s in range(4):
        new_V[s] = rewards[s] + gamma * np.sum(P[s] * V)
    V = new_V
    history.append(V.copy())
    iterations.append(i+1)

print("Final Value Function")
for s,v in zip(states,V):
    print(s,":",round(v,3))

policy = []

for s in range(4):
    if s==3:
        policy.append("Stay")
    else:
        policy.append("Move")

print("\nDerived Policy")
for s,p in zip(states,policy):
    print(s,"->",p)

history=np.array(history)

plt.figure(figsize=(8,5))
for i in range(4):
    plt.plot(iterations,history[:,i],marker='o',label=states[i])

print("===== SUMMARY =====")
print("Bellman Equation : V(s) = R(s) + γ Σ P(s,s')V(s')")
print("Discount Factor :", gamma)
print("Number of States :", len(states))
print("Iterations :", len(iterations))
print()

plt.xlabel("Iterations")
plt.ylabel("State Value")
plt.title("Bellman Value Function Convergence")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(6,4))
plt.bar(states,V)
plt.title("Final Value Function")
plt.ylabel("Value")
plt.show()
