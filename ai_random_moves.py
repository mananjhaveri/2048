from gameplay import game 
import os 
import time 
import random 
import csv

obj = game() 
state = obj.get_initial_state()
score = 0

moves = ["w", "a", "s", "d"] 
temp_score = 0
random_move = None
d = {"w": 0.35, "a": 0.35, "s": 0.1, "d": 0.2}
absolute_random = False

while True:
    obj.display(state, score)

    possible_moves = obj.get_possible_moves(state)
    if possible_moves == []:
        break
    
    if absolute_random:
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

weights = ""
for k,v in d.items():
    weights += "_" + str(k) + str(v) 

# append data in csv file
if absolute_random == True:
    filename = "absolute_random_moves.csv"
else:
    filename = "weighted_random_moves" + weights + ".csv"

# add header automatically
try:
    with open("data/" + filename, "r") as f:
        reader = csv.reader(f)
        for header in reader:
            break
except:
    fields = ["score", "max_element"]
    with open("data/" + filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

fields = [score, max_]
with open("data/" + filename, 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)