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


RRHC(8)



