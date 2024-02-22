class board:

    def __init__(self, height, width):
        # TODO : Define variables as needed
        self.height = height
        self.width = width
        self.board = []
        print("This be working")

    def boardmatrix(self):
        self.board = [['  ' for i in range(self.height+2)] for j in range(self.width+2)]
        self.board[0][0] = '+ '
        self.board[0][self.width+1] = '+ '
        self.board[self.height+1][0] = '+ '
        self.board[self.height+1][self.width+1] = '+ '

        for i in range(1, self.width+1):
            self.board[0][i] = "──"
            self.board[self.width+1][i] = "──"
        for j in range(1, self.height+1):
            self.board[j][0] = "| "
            self.board[j][self.height+1] = "| "

    def render(self):
        # TODO: Initialize the board and display on the commandline
        self.boardmatrix()
        
        for i in range(self.width+2):
            for j in range(self.height+2):
                print(' '.join(self.board[i][j]), end="")
            print()

board = board(10,10)
board.render()
board.boardmatrix()
