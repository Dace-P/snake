class board:
    height = 0
    width = 0

    def __init__(self, height, width):
        # TODO : Implement sizes according to the provided parameters
        self.height = height
        self.width = width
        print("This be working")

    def render(self):
        # TODO: Initialize the size of the 
        print("The height is: " + str(self.height))
        print("The width is: " + str(self.width))
        print("This also be working")

board = board(10,15)
board.render()