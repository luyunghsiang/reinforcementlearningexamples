'''
Practice for reinforcement leanring of the Frozen Lake game
The game has m x n cells (usually 4 x 4) marked as S, G, F, and H
S: starting point
G: Goal
F: Frozen (walk way)
H: Hole (fail)
This version does not consider slippery surface.
'''
'''
Acceptable actions: 
0: up
1: down
2: left
3: right
'''
class Board:
    def __init__(self):
        self.rewards = [1, 0, -1,
                      -1, -10, -1,
                       0, -1, 10
                      ]
        l = len(self.rewards)
        self.qval = [[0 for s in range(l)] for a in range (4)]
        self.length = l
        self.epsilon = 1 # ratio of exploration, gradually decrease
        self.alpha = 0.7 # learning rate
        self.maxstep = 1000
        self.location = 6 # initial location at cell 6

    def nextcell(self, dir):
        # return True if this move is valid, False if invalid
        if (dir == 0): # up
            if (self.location >= 3):
                self.location = self.location -3
                return True
            else:
                return False
        if (dir == 1): # down
            if (self.location < 6):
                self.location = self.location + 3
                return True
            else:
                return False
        if (dir == 2): # left
            if ((self.location % 3) != 0):
                self.location = self.location - 1
                return True
            else:
                return False
        if (dir == 3): # right
            if ((self.location % 3) != 2):
                self.location = self.location + 1
                return True
            else:
                return False
    def updateqval(self):
        for l in range(self.length):
            for a in range (4):

    def move(self):
        done = False
        while (done == False):
            self.updateqval()

if __name__ == '__main__':
    br = Board()
    br.move()