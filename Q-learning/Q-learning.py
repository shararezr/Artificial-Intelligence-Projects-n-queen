#!/usr/bin/env python3.6
import numpy as np
import random


# Initialize q-table values to 0

action = {0: 'N', 1: 'S', 2: 'E', 3: 'W'}
state_size = 20
action_size = 4
Rl = np.array([-8, -8, -8, -8, -8, -8, 0, 0, 0, 8, -
               8, 0, 0, 0, -8, -8, -8, -8, -8, -8])
Q = np.zeros((action_size, state_size))
print(Q)
state = 0
act = 0
eplison = 0.2
alpha = 0.8
D_factor = 0.9
next_state = 0
num_episodes = 100


def _nextstate_(a, s):
    if(action[a] == 'N' and 4 <= s <= 19):
        next_state = s-5
        
    elif (action[a] == 'S' and 0 <= s <= 14):
        next_state = s+5
        
    elif (action[a] == 'E' and s != 19 and s!=14 and s!=9 and s!=4):
        next_state = s+1
        
    elif (action[a] == 'W' and s != 0 and s!=5 and s!=10 and s!=15):
        next_state = s-1
        
    elif (action[a] == 'S' and 14<= s <= 19):
        next_state = s-5
    elif(action[a] == 'N' and 0 <= s <= 4):
        next_state = s+5
    elif (action[a] == 'E' and (s == 19 or s==14 or s==9 or s==4)):
        next_state = s-1
    elif (action[a] == 'W' and (s == 0 or s==5 or s==10 or s==15)):
        next_state = s+1
    return(next_state)





for ith_episode in range(num_episodes):
    num_actions = random.randint(4, 10)
    for ith_action in range(num_actions):
        # set the percent you want to explore, epsilon=0.2
        if random.uniform(0, 1) < eplison:
            # explore select a random action
            act = random.randint(0, 3)
            state = random.randint(0, 19)
            next_state = _nextstate_(act, state)
            best_next_action = Q[0][next_state]
            for j in range(1,3):
                if (Q[j-1][next_state] <= Q[j][next_state]).any():
                    best_next_action = Q[j][next_state]
            Q[act][state] = Q[act][state]+alpha * \
                (Rl[next_state] + D_factor*best_next_action-Q[act][state])

        else:
            # exploit select the action with  max value()
            state = random.randint(0, 19)
            next_state = _nextstate_(0, state)
            act = 0
            best_next_action = Q[0][next_state]
            for j in range(1,3):
                if (Q[j-1][next_state] <= Q[j][next_state]).any():
                    best_next_action = Q[j][next_state]
            
            max_item = Q[act][state]+alpha * \
                (Rl[next_state]+D_factor*best_next_action-Q[act][state])

            for i in range(1, 3):
                next_state = _nextstate_(i, state)
                best_next_action = Q[0][next_state]
                for j in range(1,3):
                    if (Q[j-1][next_state] <= Q[j][next_state]).any():
                        best_next_action = Q[j][next_state]
                current_item = Q[i][state]+alpha * \
                    (Rl[next_state]+D_factor*best_next_action-Q[i][state])
                if (max_item <= current_item).any():
                    max_item = current_item
                    act = i
            next_state = _nextstate_(act, state)
            best_next_action = Q.max(0)[next_state]
            Q[act][state] = Q[act][state] + alpha * \
                (Rl[next_state] + D_factor*best_next_action - Q[act][state])

    print ("Q-table in {} episode :".format(ith_episode))
    print(Q)
