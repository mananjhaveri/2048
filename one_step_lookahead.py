from gameplay import game 
import os 
import time 
import random 
import copy 
import csv

obj = game() 
state = obj.get_initial_state()
score = 0

while True:    
    obj.display(state, score)

    possible_moves = obj.get_possible_moves(state)
    if possible_moves == []:
        break

    d = {}

    for move in possible_moves:
        current_state = copy.deepcopy(state)
        _, __, t_score = obj.move(current_state, move)
        d[move] = t_score 

    d = {i: j for i, j in sorted(d.items(), key= lambda x: x[1], reverse=True)}
    best_score = list(d.values())[0] 

    best_moves = []
    for i, j in d.items():
        if j == best_score:
            best_moves.append(i)

    
    if "w" in best_moves:
        best_move = "w"
    elif "a" in best_moves:
        best_move = "a"
    else:
        best_move = random.choices(best_moves)[0]


    _, state, temp_score = obj.move(state, best_move) 
    score += temp_score 

    # _ = os.system('cls')

max_ = 0 
for row in state:
    if max_ < max(row):
        max_ = max(row)
print("GAME OVER!!!", score, max_)

# append data in csv file
fields = [score, max_]
with open("data/one_step_lookahead.csv", 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)