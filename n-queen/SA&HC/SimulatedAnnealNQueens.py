#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time
import math

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


RRSA(8)