class Board:
    def __init__(self):
        self.cells = [[' ' for c in range(3)] for r in range (3)]
        self.resetscore()
    def resetscore(self):
        self.Xwin = 0
        self.Owin = 0
        self.draw = 0
    def printscores(self):
        print('Xwin = ', str(self.Xwin), end = '')
        print(' Owin = ', str(self.Owin), end = '')
        print(' draw = ', str(self.draw))
    def printcells(self):
        print(self.cells[0])
        print(self.cells[1])
        print(self.cells[2])
    def generate(self):
        for row in range(3):
            for col in range(3):
                self.cells[row][col] = 'O'
                self.generate_helper(8, 'X')
                print('O at', str(row), str(col))
                self.printscores()
                self.resetscore()
                self.cells[row][col] = 'X'
                self.generate_helper(8, 'O')
                print('X at', str(row), str(col))
                self.printscores()
                self.cells[row][col] = ' '  # reset to empty

    def generate_helper(self, numleft, turn):
        # print(self.cells, numleft, turn)
        if (numleft == 0):
            # print('filled ==>', self.cells)
            # self.printcells()
            self.win()
            return
        if (turn == 'X'):
            nextturn = 'O'
        if (turn == 'O'):
            nextturn = 'X'
        for row in range(3):
            for col in range(3):
                if (self.cells[row][col] == ' '):
                    # print('fill ', str(row), str(col), 'by ', turn)
                    self.cells[row][col] = turn
                    # self.printcells()
                    self.generate_helper(numleft - 1, nextturn)
                    self.cells[row][col] = ' ' # reset
                    # print('UN fill ', str(row), str(col), self.cells, str(numleft))
    def updatescore(self, turn):
        if (turn == 'X'):
            self.Xwin = self.Xwin + 1
        elif (turn == 'O'):
            self.Owin = self.Owin - 1
        else:
            self.draw = self.draw + 1
    def win(self):
        # check row
        for row in range(3):
            if (self.cells[row][0] == self.cells[row][1]):
                if (self.cells[row][1] == self.cells[row][2]):
                    self.updatescore(self.cells[row][0])
                    return
        # check column
        for col in range(3):
            if (self.cells[0][col] == self.cells[1][col]):
                if (self.cells[1][col] == self.cells[2][col]):
                    self.updatescore(self.cells[0][col])
                    return
        # check diagnoal
        if (self.cells[0][0] == self.cells[1][1]):
                if (self.cells[1][1] == self.cells[2][2]):
                    self.updatescore(self.cells[0][0])
                    return
        # draw
        self.updatescore(' ')
if __name__ == '__main__':
    br = Board()
    br.generate()
