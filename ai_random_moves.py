from gameplay import game 
import os 
import time 
import random 

obj = game() 

moves = ["w", "a", "s", "d"] 
d = {}
temp_score = 0
random_move = None
while True:
    print("CURRENT SCORE:", obj.score, "\n")
    print(random_move)
    for i in obj.mat:
        for j in i:
            temp = str(j)
            for l in range(5 - len(temp)):
                temp = " " + temp 
            
            print(temp, end=" ")
        print() 

    random_move = random.choice(moves)[0]
    # print(random_move)
    ret = obj.move(random_move)
    # time.sleep(1)
    
    if ret == -1:  
        if obj.score != temp_score:
            d = {}

        temp_score = obj.score
        d[random_move] = 1 
        print(d)
        time.sleep(5)        
    
    if len(d) == 4:
        break 

    _ = os.system('cls')

print("GAME OVER!!!")