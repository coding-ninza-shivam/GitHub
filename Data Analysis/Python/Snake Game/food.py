import turtle
import random

class Food(turtle.Turtle):
    def __init__(self, screen_width, screen_height, grid_size):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.grid_size = grid_size
        self.shape("circle")
        self.penup()
        self.speed(0) 
        self.color("red")
        self.shapesize(stretch_wid=grid_size / 20, stretch_len=grid_size / 20)
        self.position = self.randomize_position()
        self.goto(self.position)

    def randomize_position(self):
        """
        Generates a random position for the food on the grid.
        """
        x = random.randrange(-(self.screen_width // 2) // self.grid_size + 1, (self.screen_width // 2) // self.grid_size) * self.grid_size
        y = random.randrange(-(self.screen_height // 2) // self.grid_size + 1, (self.screen_height // 2) // self.grid_size) * self.grid_size
        return (x, y)

    def move(self):
        """
        Moves the food to a new random position.
        """
        self.position = self.randomize_position()
        self.goto(self.position)