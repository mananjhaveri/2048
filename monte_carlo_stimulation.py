import copy 
import random
import time 
from gameplay import * 

total_simulation = 200

def monte_carlo(current_state):
    
    possible_moves = obj.get_possible_moves(current_state)
    d = {}

    for move in possible_moves:
        for ctr in range(total_simulation // len(possible_moves)):
            state = copy.deepcopy(current_state) 
            game_end, state, score = obj.move(state, move)
            total_score = score
            while game_end != -1:
                new_possible_moves = obj.get_possible_moves(state)
                if len(new_possible_moves) == 0:
                    break
                random_move = random.choices(new_possible_moves)
                game_end, state, score = obj.move(state, random_move[0])
                total_score += score 
        
        d[move] = total_score
    
    return d 


if __name__ == "__main__":
    obj = game() 
    state = obj.get_initial_state()
    total_score = 0 

    start_time = time.time()
    while True:
        obj.display(state, total_score)

        d = monte_carlo(state)
        max_ = -1
        best_move = None
        for k, v in d.items():
            if v > max_:
                best_move = k 
                max_ = v  

        if best_move == None:
            break 
        
        print("best_move", best_move)
        game_end, state, score = obj.move(state, best_move)
        total_score += score  

        if game_end == -1:
            break   

    end_time = time.time()
    print("time taken:", end_time - start_time)

    max_ = 0 
    for row in state:
        if max_ < max(row):
            max_ = max(row)
    print("GAME OVER!!!", total_score, max_)

    obj.display(state, str(total_score) + " | GAME OVER!!!")
    input()



    




