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
d = {"w": 0.35, "a": 0.35, "s": 0.1, "d": 0.2}
absolut_random = True

while True:
    obj.display(state, score)

    possible_moves = obj.get_possible_moves(state)
    if possible_moves == []:
        break
    
    if absolut_random:
        random_move = random.choices(possible_moves)[0]
    else:
        weights = [d[i] for i in possible_moves]
        random_move = random.choices(possible_moves, weights=weights)[0]    

    _, state, temp_score = obj.move(state, random_move)
    score += temp_score 

    # time.sleep(5)   
    # _ = os.system('cls')

max_ = 0
for row in state:
    if max_ < max(row):
        max_ = max(row)
print("GAME OVER!!!", score, max_)