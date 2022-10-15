from typing import List, Any


class Board:  # one particular state of the game
    def __init__(self, loc, symbol, filled=None):
        self.cells = [' ' for c in range(9)]
        if (filled != None):
            for c in range(9):
                self.cells[c] = filled[c]
        if (self.cells[loc] != ' '):
            print('Error, already filled')
        self.cells[loc] = symbol
        self.win = '-'
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

    def mirrorV(self): # mirror vertically
        cells = [' ' for c in range(9)]
        cells[0] = self.cells[6]
        cells[1] = self.cells[7]
        cells[2] = self.cells[8]
        cells[3] = self.cells[3]
        cells[4] = self.cells[4]
        cells[5] = self.cells[5]
        cells[6] = self.cells[0]
        cells[7] = self.cells[1]
        cells[8] = self.cells[2]
        self.cells = cells

    def mirrorH(self): # mirror horizontally
        cells = [' ' for c in range(9)]
        cells[0] = self.cells[2]
        cells[1] = self.cells[1]
        cells[2] = self.cells[0]
        cells[3] = self.cells[5]
        cells[4] = self.cells[4]
        cells[5] = self.cells[3]
        cells[6] = self.cells[8]
        cells[7] = self.cells[7]
        cells[8] = self.cells[6]
        self.cells = cells

    def rotateequivalent(self, br):
        if (self.cells == br.cells):  # identical
            # print('match')
            return True
        # print('rotate once: ')
        self.rotate()
        # print(self)
        if (self.cells == br.cells):
            # print('match')
            return True
        # print('rotate twice: ')
        self.rotate()
        # print(self)
        if (self.cells == br.cells):
            # print('match')
            return True
        # print('rotate three times: ')
        self.rotate()
        # print(self)
        if (self.cells == br.cells):
            # print('match')
            return True
        return False

    def equivalent(self, br):  # equivalent to br by rotation or mirror?
        # print('----------------')
        # print('original: ')
        # print(self)
        # print('compared with:')
        # print(br)
        if (self.rotateequivalent(br) == True):
            return True
        # print('vertical mirror:')
        self.mirrorV()
        if (self.rotateequivalent(br) == True):
            return True
        # print('horizontal mirror:')
        self.mirrorH()
        if (self.rotateequivalent(br) == True):
            return True
        # print('not match')
        return False
    '''
    
    def updatescore(self, turn):
        if (turn == 'X'):
            self.Xwin = self.Xwin + 1
        elif (turn == 'O'):
            self.Owin = self.Owin - 1
        else:
            self.draw = self.draw + 1
    '''
    def decidewin(self):
        # check row
        for row in range(3):
            col0 = self.cells[3 * row]
            col1 = self.cells[3 * row + 1]
            col2 = self.cells[3 * row + 2]
            if ((col0 == col1) and (col1 == col2) and (col0 != ' ')):
                self.win = col0
                return True
        # check column
        for col in range(3):
            row0 = self.cells[col]
            row1 = self.cells[col + 3]
            row2 = self.cells[col + 6]
            if ((row0 == row1) and (row1 == row2) and (row0 != ' ')):
                self.win = row0
                return True
        # check diagnoal
        dia0 = self.cells[0]
        dia1 = self.cells[4]
        dia2 = self.cells[8]
        if ((dia0 == dia1) and (dia1 == dia2) and (dia0 != ' ')):
            self.win = dia0
            return True
        dia0 = self.cells[2]
        dia1 = self.cells[4]
        dia2 = self.cells[6]
        if ((dia0 == dia1) and (dia1 == dia2) and (dia0 != ' ')):
            self.win = dia0
            return True
        # no winner yet
        return False
    '''
    def resetscore(self):
        self.Xwin = 0
        self.Owin = 0
        self.draw = 0

    def printscores(self):
        print('Xwin = ', str(self.Xwin), end='')
        print(' Owin = ', str(self.Owin), end='')
        print(' draw = ', str(self.draw))
    '''
    def __str__(self):
        val = str(self.cells[0:3]) + '\n'
        val += str(self.cells[3:6]) + '\n'
        val += str(self.cells[6:9]) + '\n'
        self.decidewin()
        val += 'winner: ' + self.win + '\n'
        return val


class Game:
    board: List[Any]

    def __init__(self):
        self.board = [[] for n in range(9)]
        self.turn = ['X', 'O']
    def generate(self):
        for loc in range(9):
            # print('loc = ', str(loc))
            br = Board(loc, self.turn[0])
            # print(br)
            addnew = True
            for prev in range(len(self.board[0])):
                if (br.equivalent(self.board[0][prev]) == True):
                    # print('find equivalent')
                    addnew = False
            if (addnew == True):
                self.board[0].append(br)
        # print('print distinct boards:')
        # for loc in range(len(self.board[0])):
            # print(self.board[0][loc])
        for numfilled in range(1, 9):
            numprev = len(self.board[numfilled - 1])
            for loc in range(numprev):
                self.generate_helper(numfilled)
        for numfilled in range(9):
            numboard = len(self.board[numfilled])
            print(str(numboard), 'boards with', str(numfilled + 1))
            for loc in range(numboard):
                print(self.board[numfilled][loc])

    def generate_helper(self, numfilled):
        # print('generate_helper', str(numfilled))
        for ind in range(len(self.board[numfilled - 1])):
            brorig = self.board[numfilled - 1][ind]  # original board
            for loc in range(9):
                addnew = True
                if ((brorig.cells[loc] == ' ') and (brorig.win == ' ')):
                    # not used yet and no winner yet
                    br = Board(loc, self.turn[numfilled % 2], brorig.cells)
                    for prev in range(len(self.board[numfilled])):
                        if (br.equivalent(self.board[numfilled][prev]) == True):
                            # print('find equivalent')
                            addnew = False
                    if (addnew == True):
                        self.board[numfilled].append(br)
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
