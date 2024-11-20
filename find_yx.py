import random

class Get_X_Y:
    def __init__(self):
        self.HEIGHT = 500
        self.mitte = self.HEIGHT / 2            
        self.x1 = 0
        self.x2 = 0
        self.x3 = 0
        self.x4 = 0
        self.x5 = 0      
    
    def return_x1(self):
        self.x1 = random.randint(0, self.mitte - 120)
        return self.x1
    
    def return_x2(self):
        self.x2 = random.randint(self.mitte, self.HEIGHT - 120)
        return self.x2
    
    def return_x3(self):
        self.x3 = random.randint(self.mitte / 2, self.HEIGHT / 4 * 3 - 120)
        return self.x3
    
    def return_x4(self):
        self.x4 = random.randint(0, self.mitte - 120)
        return self.x4
    
    def return_x5(self):
        self.x5 = random.randint(self.mitte, self.HEIGHT - 120)
        return self.x5