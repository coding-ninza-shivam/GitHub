# snake.py
import turtle

class Snake:
    def __init__(self, grid_size):
        self.grid_size = grid_size  # Store grid_size as an instance variable
        self.segments = []
        self.head = self.create_segment(0, 0) # Initial head at the center
        self.direction = "Right"
        self.speed = grid_size

    def create_segment(self, x, y):
        """Creates a new segment for the snake."""
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.speed(0)
        new_segment.shapesize(stretch_wid=self.grid_size / 20, stretch_len=self.grid_size / 20) # Use self.grid_size
        new_segment.goto(x, y)
        self.segments.append(new_segment)
        return new_segment

    def move(self):
        """Moves the snake."""
        if not self.segments:
            return

        # Move the tail segments first in reverse order
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)

        # Move the head
        if self.direction == "Up":
            self.head.sety(self.head.ycor() + self.speed)
        elif self.direction == "Down":
            self.head.sety(self.head.ycor() - self.speed)
        elif self.direction == "Left":
            self.head.setx(self.head.xcor() - self.speed)
        elif self.direction == "Right":
            self.head.setx(self.head.xcor() + self.speed)

    def grow(self):
        """Adds a new segment to the snake's tail."""
        last_segment = self.segments[-1]
        new_segment = self.create_segment(last_segment.xcor(), last_segment.ycor())

    def change_direction(self, new_direction):
        """Changes the direction of the snake, preventing immediate 180-degree turns."""
        if new_direction == "Up" and self.direction != "Down":
            self.direction = new_direction
        elif new_direction == "Down" and self.direction != "Up":
            self.direction = new_direction
        elif new_direction == "Left" and self.direction != "Right":
            self.direction = new_direction
        elif new_direction == "Right" and self.direction != "Left":
            self.direction = new_direction

    def check_collision(self, screen_width, screen_height):
        """Checks for collision with walls and itself."""
        head_x = self.head.xcor()
        head_y = self.head.ycor()

        # Wall collision
        if head_x > (screen_width / 2) - (self.grid_size / 2) or head_x < -(screen_width / 2) + (self.grid_size / 2) or \
           head_y > (screen_height / 2) - (self.grid_size / 2) or head_y < -(screen_height / 2) + (self.grid_size / 2):
            return True

        # Self-collision
        for segment in self.segments[1:]:
            if self.head.distance(segment) < self.grid_size / 2: # Check if head is close to any other segment
                return True

        return False

    def reset(self):
        """Resets the snake to its initial state."""
        for seg in self.segments:
            seg.goto(1000, 1000) # Move segments off-screen
        self.segments.clear()
        self.head = self.create_segment(0, 0)
        self.direction = "Right"
