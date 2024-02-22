class snake:
    def __init__(self, headx, heady):
        self.body = [[headx, heady]]
        #self.direction = direction
    
    def take_step(self):
        print()

    def set_direction(self):
        print()
    
    def head(self):
        return self.body[0]
    
snake = snake(1,2)
print(snake.head())