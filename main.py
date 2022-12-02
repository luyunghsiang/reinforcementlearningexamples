# This program builds the graph of all possible Tic-Tac-Toe states


class Graph:
    def __init__(self):

class Board:
    def __init__(self):
        self.cells = [' ' for c in range(9)]
    def rotate(self):   # clockwise
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




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
