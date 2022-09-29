from typing import List, Any


class Board:  # one particular state of the game
    def __init__(self, loc, symbol, filled=None):
        self.cells = [' ' for c in range(9)]
        if (filled != None):
            for c in range(9):
                self.cells[c] = filled[c]
        if (self.cells[loc] != ' '):
            printf('Error, already filled')
        self.cells[loc] = symbol

    def rotate(self):  # clockwise
        '''
        original:
        0 1 2
        3 4 5
        6 7 8
        new
        6 3 0
        7 4 1
        8 5 2
        '''
        cells = [' ' for c in range(9)]
        cells[0] = self.cells[6]
        cells[1] = self.cells[3]
        cells[2] = self.cells[0]
        cells[3] = self.cells[7]
        cells[4] = self.cells[4]
        cells[5] = self.cells[1]
        cells[6] = self.cells[8]
        cells[7] = self.cells[5]
        cells[8] = self.cells[2]
        self.cells = cells

    def equivalent(self, br):  # equivalent to br by rotation or mirror?
        print('original: ')
        print(self)
        if (self.cells == br.cells):  # identical
            return True
        self.rotate()  # rotate once
        print('rotate once: ')
        print(self)
        if (self.cells == br.cells):
            return True
        self.rotate()  # rotate twice
        print('rotate twice: ')
        print(self)
        if (self.cells == br.cells):
            return True
        self.rotate()  # rotate third time
        print('rotate three times: ')
        print(self)
        if (self.cells == br.cells):
            return True
        return False

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

    def resetscore(self):
        self.Xwin = 0
        self.Owin = 0
        self.draw = 0

    def printscores(self):
        print('Xwin = ', str(self.Xwin), end='')
        print(' Owin = ', str(self.Owin), end='')
        print(' draw = ', str(self.draw))

    def __str__(self):
        val = str(self.cells[0:3]) + '\n'
        val += str(self.cells[3:6]) + '\n'
        val += str(self.cells[6:9]) + '\n'
        return val


class Game:
    board: List[Any]

    def __init__(self):
        self.board = []

    def generate(self):
        for loc in range(9):
            print('loc = ', str(loc))
            br = Board(loc, 'X')
            print(br)
            addnew = True
            for prev in range(len(self.board)):
                if (br.equivalent(self.board[prev]) == True):
                    print('find equivalent')
                    addnew = False
            if (addnew == True):
                self.board.append(br)
        print('print distinct boards:')
        for loc in range(len(self.board)):
            print(self.board[loc])

    '''
    
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
    '''


if __name__ == '__main__':
    gm = Game()
    gm.generate()
