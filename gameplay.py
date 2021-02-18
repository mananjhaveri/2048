import random 
import os

class game():

    def __init__(self):
        self.mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 
        self.score = 0 
        count = 0
        while count < 2:
            a, b = self.get_random_position(), self.get_random_position()
            if self.mat[a][b] == 0:
                self.mat[a][b] = self.get_random_element()
                count += 1
           
    def get_random_element(self):
        return random.choices([2, 4], weights=(0.9, 0.1))[0] 
    
    def get_random_position(self):
        return random.choices([0, 1, 2, 3])[0]

    def rotate(self):
        temp = self.mat.copy()
        self.mat = []
        for i in range(4):
            col = []
            for j in range(1, 5):
                col.append(temp[-j][i])
            self.mat.append(col)
    
    def swipe(self):

        flag = False
        
        for t in range(4): 
            for i in range(3):
                for j in range(4):
                    if self.mat[i][j] == 0:
                        self.mat[i][j], self.mat[i+1][j] = self.mat[i+1][j], 0
                        flag = True 

        
        for i in range(3):
            for j in range(4):  
                if self.mat[i][j] == self.mat[i+1][j]:
                    self.mat[i][j] += self.mat[i+1][j]
                    self.mat[i+1][j] = 0
                    self.score += self.mat[i][j]
                    flag = True 

        for t in range(4): 
            for i in range(3):
                for j in range(4):
                    if self.mat[i][j] == 0:
                        self.mat[i][j], self.mat[i+1][j] = self.mat[i+1][j], 0 
        
        return flag 
        
    
    def move(self, direction):
        if direction == "w":
            flag = self.swipe()
        elif direction == "s":
            self.mat.reverse()
            flag = self.swipe()
            self.mat.reverse() 
        elif direction == "a":
            self.rotate()
            flag = self.swipe()
            for i in range(3):
                self.rotate()
        else:
            for i in range(3):
                self.rotate()
            flag = self.swipe()
            self.rotate()         

        # check if game over
        if not flag:
            return -1

        # if game not over, add random element 
        d = {} 
        while True:
            print("---------------------------------------------------------")
            a, b = self.get_random_position(), self.get_random_position()
            d[(a, b)] = 1 

            if self.mat[a][b] == 0:
                self.mat[a][b] = self.get_random_element()
                break 
            
            if len(d) == 16:
                break 
        
        return None


"""
obj = game()

while True:
    print("CURRENT SCORE:", obj.score, "\n")
    for i in obj.mat:
        for j in i:
            temp = str(j)
            for l in range(5 - len(temp)):
                temp = " " + temp 
            
            print(temp, end=" ")
        print()
        

    direction = input().lower()
    ret = obj.move(direction)
    if ret == -1:
        print("invalid move") 

    _ = os.system('cls')


print("GAME OVER")


"""