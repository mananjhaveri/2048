import random 
import os
import copy 

class game():

    def get_initial_state(self):
        state = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 
        count = 0
        while count < 2:
            a, b = self.get_random_position(), self.get_random_position()
            if state[a][b] == 0:
                state[a][b] = self.get_random_element()
                count += 1         
        return state
           
    def get_random_element(self):
        return random.choices([2, 4], weights=(0.9, 0.1))[0] 
    
    def get_random_position(self):
        return random.choices([0, 1, 2, 3])[0]

    def rotate(self, state):
        temp = state.copy()
        state = []
        for i in range(4):
            col = []
            for j in range(1, 5):
                col.append(temp[-j][i])
            state.append(col) 
        return state
    
    def swipe(self, state):
        score = 0 
        flag = False
        
        for t in range(4): 
            for i in range(3):
                for j in range(4):
                    if state[i][j] == 0:
                        if state[i+1][j] != 0:
                            flag = True
                        state[i][j], state[i+1][j] = state[i+1][j], 0
                        

        
        for i in range(3):
            for j in range(4):  
                if state[i][j] == state[i+1][j] and state[i+1][j] != 0:
                    state[i][j] += state[i+1][j]
                    state[i+1][j] = 0
                    score += state[i][j]
                    flag = True 

        for t in range(4): 
            for i in range(3):
                for j in range(4):
                    if state[i][j] == 0:
                        state[i][j], state[i+1][j] = state[i+1][j], 0 
        
        return flag, state, score 
        
    
    def move(self, state, direction, place_element=True):
        if direction == "w":
            flag, state, score = self.swipe(state)
        elif direction == "s":
            state.reverse()
            flag, state, score = self.swipe(state)
            state.reverse() 
        elif direction == "a":
            state = self.rotate(state)
            flag, state, score = self.swipe(state)
            for i in range(3):
                state = self.rotate(state)
        elif direction == "d":
            for i in range(3):
                state = self.rotate(state)
            flag, state, score = self.swipe(state)
            state = self.rotate(state)         

        # check if game over
        if not flag:
            return -1, state, score
        
        if place_element:
            self.place_random_element(state)
        return None, state, score 

    def place_random_element(self, state):
        d = {} 
        while True:
            a, b = self.get_random_position(), self.get_random_position()
            d[(a, b)] = 1 

            if state[a][b] == 0:
                state[a][b] = self.get_random_element()
                break 
            
            if len(d) == 16:
                break 

        return state    
        
        

    def get_possible_moves(self, state):
        moves = ["w", "a", "s", "d"] 
        possible_moves = [] 

        for move in moves:
            temp_state = copy.deepcopy(state)
            t_flag, _, __ = self.move(temp_state, move) 
            if t_flag != -1:
                possible_moves.append(move)
        
        return possible_moves






# obj = game()
# state = obj.get_initial_state()
# score = 0
# while True:
#     print("CURRENT SCORE:", score, "\n")
#     for i in state:
#         for j in i:
#             temp = str(j)
#             for l in range(5 - len(temp)):
#                 temp = " " + temp 
            
#             print(temp, end=" ")
#         print()
        

#     direction = input().lower() 
#     if direction in obj.get_possible_moves(state):
#         _, state, temp_score = obj.move(state, direction)
#         score += temp_score

#     _ = os.system('cls')


# print("GAME OVER")


