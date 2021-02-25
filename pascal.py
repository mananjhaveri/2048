from gameplay import game 
import os 
import time 
import random 
import copy 
import csv 

def check_pascal(state):
    prev_max = 0
    curr_max = 0
    count = -1
    for i in range(4):
        for j in range(i+1):
            if state[j][i-j] > curr_max:
                curr_max = state[j][i-j]
            
            if state[j][i-j] > prev_max:
                count += 1
        prev_max = curr_max
    
    prev_max = 0
    curr_max = 0
    count -= 4
    for i in range(3, -1, -1):
        for j in range(i+1):
            if state[j][i-j] > curr_max:
                curr_max = state[j][i-j]
            
            if state[j][i-j] > prev_max:
                count += 1
        prev_max = curr_max

    return count 

a = [[32, 16, 8, 4], [4, 8, 4, 4], [8, 4, 2, 4], [4, 4, 2, 2]]
for row in a:
    print(row)
print(check_pascal(a)) 
