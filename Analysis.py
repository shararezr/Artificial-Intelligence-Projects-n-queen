#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
import time

#Step 1 - Generate a random initial state.

NumberofQ = 8
chessboard = random.sample(range(0,(NumberofQ)),(NumberofQ))

# This is how I generate my random inital state, a list of 8 values,
# each number represent the position of the queen in the respective column of the chessboard
# eg. [5,3,6,0,2,4,1,7], first number is the first queen in 5th row,1st column
# second number is the queen in the 3rd row,2nd column etc.


#Step 2 - Heuristic Function

def heuristic_function(chessboard):
  h = 0
  for x in range(len(chessboard)):
    #for every column check with every other column 
    for y in range(x + 1,len(chessboard)):
      #If two Queens are in the same row add 1
      if chessboard[x] == chessboard[y]:
        h += 1
      #Calculating the difference between the two columns to calculate the diagonal
      difference = x - y
      #For a queen to be in a diagonal, their value needs to be the 
      #the result of their value plus or minus the difference
      if chessboard[x] == chessboard[y] - difference or chessboard[x] == chessboard[y] + difference:
        h += 1
     
  return h

heuristic_function(chessboard)
##### The function returns chessboard's heuristic cost.


#Step 3/4 - Hill Climbing function

def Hill_Climbing(chessboard):
    # This for loop will change the position of one queen per column
    # and calculate the heuristic value for each move, will then store each move
    # and determine the heuristic value of the chessboard considered that move,
    # if the heuristic value is less than our original h value, will extract the moves
    # that has that value (best_moves) and pick a random one between them.
    moves = {}
    #Building a moves dictionary
    for x in range(len(chessboard)):
        for y in range(len(chessboard)):
          #Make a copy of our orig. board
          chessboard_copy = list(chessboard)
          #Move the queen to the new row
          chessboard_copy[x] = y
          #Storing the move and the heuristic value of the chessboard
          moves[(x,y)] = heuristic_function(chessboard_copy)
       
    best_moves = []
    heur_value_to_beat = heuristic_function(chessboard)
    #Iterate through moves dictionary and find the lowest heuristic value
    #when compared to our original one from the original chessboard.
    for key,value in moves.items():
        if value < heur_value_to_beat:
          heur_value_to_beat = value
    
    #Iterate through moves dictionary and find all the moves with that value
    #and store them in best_moves list.
    for key,value in moves.items():
        if value == heur_value_to_beat:
          best_moves.append(key)
       
      #Pick a random best move and return the chessboard with the chosen move.
    if len(best_moves) > 0:
        pick = random.randint(0,len(best_moves) - 1)
        x = best_moves[pick][0]
        y = best_moves[pick][1]
        chessboard[x] = y
    return chessboard

##### Adding a function to check if the algorithm has found a viable solution
def checkValid(h):
    if h != 0:
        result = 0
    else:
        result = 1
    return result

#### Making a function to return the solution if found otherwise return the best
#### possible solution available after 500 moves.
def hill(chessboard):
    for i in range(500):
        Hill_Climbing(chessboard)
        h = heuristic_function(chessboard)
        valid =checkValid(h)
    if(valid == 1):
        valid=0
        print('solution found', chessboard, 'heur cost:', h)
    else:
        print('Cannot find viable solution, best solution available:', chessboard, 'heur cost:', h)


chessboard = random.sample(range(0,(NumberofQ)),(NumberofQ))
hill(chessboard)

#Step 5 - Random Restart

def RRHC(NumberofQ):
    solution =[] # storing solution
    moves = 0 # storing moves
    t0 = time.time() # timestamp for performance evaluation
    for j in range(500): # setting a max of 500 restarts
        chessboard = random.sample(range(0,(NumberofQ)),(NumberofQ))
        for i in range(500):
            Hill_Climbing(chessboard)
            h = heuristic_function(chessboard)
            valid =checkValid(h)
            moves += 1
            if(valid == 1):
                solution.append(chessboard)
                print('Chessboard', chessboard, 'heur cost:', h)
                break
        if(valid == 1): # when solution found stop
            break
    print ('Solution found')
    t1 = time.time() # 2nd timestamp
    total = t1-t0 #differences betweent timestamps to evaluate performances
    print ('Time in seconds', total)
    print ('total cumulative moves', moves)
    return total, moves




#Step 6 - RR-SA

import math
import random

def simulated_annealing(chessboard,h,temp):
  chessboard_copy = list(chessboard) #creating a copy of original chessboard
  viable_move = False #Creating a boolean to check if a viable move has been found
 
  while not viable_move: #while a viable move hasn't been found
    chessboard_copy = list(chessboard) # copy the chessboard
    new_row = random.randint(0,len(chessboard)-1) #select a random number as a row
    new_col = random.randint(0,len(chessboard)-1) #select a random number as a column
    chessboard_copy[new_col] = new_row #apply the random move to the chessboard
    new_h = heuristic_function(chessboard_copy) # calculate the h value of the chessboard
    if new_h < h: # if the new move improves the heuristic value
      viable_move = True # then a new move has been found
    else:
      #Let's determine with what probability we can take that move
      h_difference = h - new_h #numerator for our formula
      # calculating the difference between our old h and the new h
      prob = min(1,math.exp(h_difference/temp)) # Taking the exponential to
      # the h difference divided by the temperature, higher temperature means that the choice will be more random
      # while lower temp will move the result to always accepting better h values (tending to a steepest hill alg)
      
      viable_move = random.random() <= prob
      # Will change found move to true only if our probability is bigger than a
      # random value between 0 to 1
   
  return chessboard_copy

def RRSA(NumberofQ):
    solution =[]
    moves = 0
    t0 = time.time()
    anneal_rate = 0.90 # setting an anneal rate of 90 percent
    for j in range(500): # setting a max of 500 restarts
        chessboard = random.sample(range(0,(NumberofQ)),(NumberofQ))
        temp = len(chessboard)**2 #setting the inital temp as our queens^2
        h = heuristic_function(chessboard)
        for i in range(500):
            chessboard = simulated_annealing(chessboard,h,temp)
            h = heuristic_function(chessboard)
            moves += 1
            # Will always decrease the temp by 0.90, without getting too low
            new_temp = max(temp * anneal_rate,0.01)
            temp = new_temp
            if h <= 0: # when solution found stop
                solution.append(chessboard)
                print('Chessboard', chessboard, 'heur cost:', h)
                break
        if h <= 0: # when solution found stop
            break  
    print ('Solution found')
    t1 = time.time()
    total = t1-t0
    print ('Time in seconds', total)
    print ('total cumulative moves', moves)
    return total, moves



#Step 7 - Analysis

##### 50 tries - 8 queens

RRHCtime = []
RRHCmoves = []
for x in range(50):      
    a,b = RRHC(8)
    RRHCtime.append(a)
    RRHCmoves.append(b)
    
import numpy as np
print (np.median(RRHCtime))
print (np.median(RRHCmoves))


RRSAtime = []
RRSAmoves = []
for x in range(50):      
    a,b = RRSA(8)
    RRSAtime.append(a)
    RRSAmoves.append(b)

print (np.median(RRSAtime))
print (np.median(RRSAmoves))

import matplotlib.pyplot as plt

label = ['Hill-Climbing','Annealing']
no_time = [np.median(RRHCtime),np.median(RRSAtime)
]

def plot_bar_x():
    # this is for plotting purpose
    index = np.arange(len(label))
    colors= ['coral','dodgerblue']
    plt.barh(index, no_time, color=colors)
    plt.xlabel('Time in seconds', fontsize=10)
    plt.yticks(index, label, fontsize=10, rotation=30)
    plt.title('Median time to solve 8 queens problem')
    plt.show()

plot_bar_x()

label = ['Hill-Climbing','Annealing']
no_time = [np.median(RRHCmoves),np.median(RRSAmoves)
]

def plot_bar_x():
    # this is for plotting purpose
    index = np.arange(len(label))
    colors= ['coral','dodgerblue']
    plt.barh(index, no_time, color=colors)
    plt.xlabel('Moves', fontsize=10)
    plt.yticks(index, label, fontsize=10, rotation=30)
    plt.title('Median moves to solve 8 queens problem')
    plt.show()

plot_bar_x()


           

##### Scatter plot

RRHCtimeInc = []
RRHCmovesInc = []
for x in range(4,50):      
    a,b = RRHC(x)
    RRHCtimeInc.append(a)
    RRHCmovesInc.append(b)
    
RRSAtimeInc = []
RRSAmovesInc = []
for x in range(4,50):      
    a,b = RRSA(x)
    RRSAtimeInc.append(a)
    RRSAmovesInc.append(b)
    
    
    
index = np.arange(4,50)
plt.scatter(index, RRHCtimeInc)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(index,RRHCtimeInc, s=10, c='coral', marker="s", label='RRHC')
ax1.scatter(index,RRSAtimeInc, s=10, c='dodgerblue', marker="o", label='RRSA')
plt.legend(loc='upper left')
z = np.polyfit(index, RRHCtimeInc, 1)
p = np.poly1d(z)
plt.plot(index,p(index),"r--")
print ("y=%.6fx+(%.6f)"%(z[0],z[1]))
z = np.polyfit(index, RRSAtimeInc, 1)
p = np.poly1d(z)
plt.plot(index,p(index),"b--")
plt.xlabel('No. of Queens', fontsize=10)
plt.ylabel('Time', fontsize=10)
plt.show()
print ("y=%.6fx+(%.6f)"%(z[0],z[1]))

