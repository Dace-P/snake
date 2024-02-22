class board:
    height = 0
    width = 0

    def __init__(self, height, width):
        # TODO : Define variables as needed
        self.height = height
        self.width = width
        self.board = []
        print("This be working")

    def boardmatrix(self):
        self.board = [[None]*self.width]*self.height

    def render(self):
        # TODO: Initialize the board and display on the commandline
        print("The height is: " + str(self.height))
        print("The width is: " + str(self.width))
        print("This also be working")

board = board(10,15)
board.render()
board.boardmatrix()