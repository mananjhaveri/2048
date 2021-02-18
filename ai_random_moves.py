from gameplay import game 
import os 
import time 
import random 

obj = game() 
state = obj.get_initial_state()
score = 0

moves = ["w", "a", "s", "d"] 
temp_score = 0
random_move = None
d = {"w": 0.2, "a": 0.35, "s": 0.1, "d": 0.35}

while True:
    print("CURRENT SCORE:", score, "\n")
    print(random_move)
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

    weights = [d[i] for i in possible_moves]
    random_move = random.choices(possible_moves, weights=weights)[0]    

    _, state, temp_score = obj.move(state, random_move)
    score += temp_score 

    # time.sleep(5)   
    _ = os.system('cls')

print("GAME OVER!!!")