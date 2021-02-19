from gameplay import game 
import os 
import time 
import random 
import copy 

obj = game() 
state = obj.get_initial_state()
score = 0

while True:
    print("CURRENT SCORE:", score, "\n")
    for i in state:
        for j in i:
            temp = str(j)
            for l in range(5 - len(temp)):
                temp = " " + temp             
            print(temp, end=" ")
        print() 

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

    best_move = random.choices(best_moves)[0]

    _, state, temp_score = obj.move(state, best_move) 
    score += temp_score 

    _ = os.system('cls')

print("GAME OVER!!!")