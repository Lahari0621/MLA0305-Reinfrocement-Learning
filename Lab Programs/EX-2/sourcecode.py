import numpy as np
import matplotlib.pyplot as plt

states=["S0","S1","S2","Goal"]
actions=["Move","Stay"]

gamma=0.9
theta=0.001

rewards=[-1,-2,10,0]

transition={
0:{0:[(1,1)],1:[(1,0)]},
1:{0:[(1,2)],1:[(1,1)]},
2:{0:[(1,3)],1:[(1,2)]},
3:{0:[(1,3)],1:[(1,3)]}
}

V=np.zeros(len(states))
history=[]

iteration=0

while True:
    history.append(V.copy())
    delta=0
    iteration+=1

    for s in range(len(states)):
        action_values=[]

        for a in range(len(actions)):
            value=0

            for prob,next_state in transition[s][a]:
                value+=prob*(rewards[next_state]+gamma*V[next_state])

            action_values.append(value)

        best=max(action_values)
        delta=max(delta,abs(best-V[s]))
        V[s]=best

    if delta<theta:
        history.append(V.copy())
        break

policy=[]

for s in range(len(states)):
    action_values=[]

    for a in range(len(actions)):
        value=0

        for prob,next_state in transition[s][a]:
            value+=prob*(rewards[next_state]+gamma*V[next_state])

        action_values.append(value)

    policy.append(actions[np.argmax(action_values)])

print("========== SUMMARY ==========")
print("Algorithm : Value Iteration")
print("States :",len(states))
print("Actions :",len(actions))
print("Discount Factor :",gamma)
print("Iterations :",iteration)

print("\n========== RESULT ==========")
print("Optimal Value Function\n")

for s,v in zip(states,V):
    print(s,":",round(v,3))

print("\nOptimal Policy\n")

for s,p in zip(states,policy):
    print(s,"->",p)

history=np.array(history)

plt.figure(figsize=(8,5))

for i in range(len(states)):
    plt.plot(history[:,i],marker='o',label=states[i])

plt.title("MDP Value Function Convergence")
plt.xlabel("Iterations")
plt.ylabel("State Value")
plt.grid(True)
plt.legend()

plt.figure(figsize=(6,4))
plt.bar(states,V)
plt.title("Final State Values")
plt.xlabel("States")
plt.ylabel("Value")
plt.grid(axis='y')

plt.show()
