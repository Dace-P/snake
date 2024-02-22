class board:

    def __init__(self, height, width):
        # Constructor to define dimensions, along with space for a border
        self.height = height + 2
        self.width = width + 2
        # Initializes the list for the board to be in
        self.board = []

    def boardmatrix(self):

        # Initializes the 2d list to make the board with
        self.board = [['  ' for i in range(self.width)] for j in range(self.height)] 

        # Marks the endpoints of the board
        self.board[0][0] = '+─'
        self.board[self.height-1][0] = '+─'
        self.board[0][self.width-1] = '+'
        self.board[self.height-1][self.width-1] = '+'

        # Adds the bounds of the board visibly
        for a in range(1, self.width-1):
            self.board[0][a] = '──'
            self.board[self.height-1][a] = '──'
        for b in range(1, self.height-1):
            self.board[b][0] = '| '
            self.board[b][self.width-1] = '| '

        

    def render(self):
        self.boardmatrix()

        for i in range(self.height):
            for j in range(self.width):
                print(' '.join(self.board[i][j]), end="")
            print()

board = board(10,10)
board.render()
board.boardmatrix()
