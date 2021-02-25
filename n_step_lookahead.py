from gameplay import game 
import os 
import time 
import random 
import copy 


def play_all_moves(state, parent_move, n):
    possible_moves = obj.get_possible_moves(state) 
    # print(possible_moves)
    ret = []

    for move in possible_moves:
        if n == 0:
            parent_move = move 

        current_state = copy.deepcopy(state)

        _, current_state, score = obj.move(current_state, move, False)
        parent_dict[parent_move] = parent_dict.get(parent_move, 0) + score

        for i in range(4):
            for j in range(4):
                temp_state = copy.deepcopy(current_state)
                if current_state[i][j] == 0:
                    for e in [2, 4]:   
                        temp_state[i][j] = e  
                        ret.append((copy.deepcopy(temp_state), parent_move)) 
    
    return ret
        


def n_step_rec(state, parent_move="", n=0):
    if n == N:
        return  
    else:
        all_states = play_all_moves(state, parent_move, n)
        for new_state, p_move in all_states:
            n_step_rec(new_state, p_move, n + 1) 

N = 2
obj = game() 
state = obj.get_initial_state()
score = 0

while True:
    obj.display(state, score)
    # time.sleep(5)

    possible_moves = obj.get_possible_moves(state)
    if possible_moves == []:
        break 

    parent_dict = {}
    n_step_rec(state)

    parent_dict = {i: j for i, j in sorted(parent_dict.items(), key= lambda x: x[1], reverse=True)}
    best_score = list(parent_dict.values())[0] 

    best_moves = []
    for i, j in parent_dict.items():
        if j == best_score:
            best_moves.append(i)


    best_move = random.choices(best_moves)[0]

    _, state, temp_score = obj.move(state, best_move) 
    score += temp_score 
    
    # count = 0
    # for row in state:
    #     count += row.count(0)

    # if count >= 8 or score < 3000:
    #     N = 2
    # elif count >= 4:
    #     N = 3 
    # elif count >=2:
    #     N = 4
    # else:
    #     N = 5

    # if score > 3000:
    #     N = 3
    # elif score > 10000:
    #     N = 4

    _ = os.system('cls')

obj.display(state, str(score) + " || GAME OVER!!!")
# time.sleep(10)
print("GAME OVER!!!", score)