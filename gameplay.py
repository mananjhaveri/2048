import random 
import os

class game():

    def __init__(self):
        self.mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 
        self.score = 0 
        for i in range(2):
            a, b = random.choices([0, 1, 2, 3])[0], random.choices([0, 1, 2, 3])[0]
            c = random.choices([2, 4], weights=(0.9, 0.1))[0]
            self.mat[a][b] = c
           
    def get_random_element(self):
        return random.choices([2, 4], weights=(0.9, 0.1)) 
    
    def get_random_position(self):
        return random.choices([0, 1, 2, 3])

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

        
        for i in range(3):
            for j in range(4):  
                if self.mat[i][j] == self.mat[i+1][j]:
                    self.mat[i][j] += self.mat[i+1][j]
                    self.mat[i+1][j] = 0
                    self.score += self.mat[i][j]

        for t in range(4): 
            for i in range(3):
                for j in range(4):
                    if self.mat[i][j] == 0:
                        self.mat[i][j], self.mat[i+1][j] = self.mat[i+1][j], 0
        
    
    def move(self, direction):
        if direction == "w":
            self.swipe()
        elif direction == "b":
            self.mat.reverse()
            self.swipe()
            self.mat.reverse() 
        elif direction == "a":
            self.rotate()
            self.swipe()
            for i in range(3):
                self.rotate()
        else:
            for i in range(3):
                self.rotate()
            self.swipe()
            self.rotate()         

        # check if game over
        for i in range(4):
            count = 0
            if not 0 in self.mat[i]:
                count += 1
            else:
                break 

        if count == 4:
            return -1 

        # if game not over, add random element 
        while True:
            a, b = self.get_random_position()[0], self.get_random_position()[0]
            if self.mat[a][b] == 0:
                self.mat[a][b] = self.get_random_element()[0]
                break 
        
        return None
                        
obj = game()

while True:
    print("CURRENT SCORE:", obj.score, "\n")
    for i in obj.mat:
       print(i)
    print()

    direction = input().lower()
    ret = obj.move(direction)
    if ret == -1:
        break 

    _ = os.system('cls')


print("GAME OVER")


