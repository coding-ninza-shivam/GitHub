import turtle
import time
from snake import Snake
from food import Food

# Screen setup
screen_width = 600
screen_height = 480
grid_size = 20
game_speed = 0.15 
score_file = "score.txt"

screen = turtle.Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("Turtle Snake Game")
screen.tracer(0)

# Create game objects
snake = Snake(grid_size)
food = Food(screen_width, screen_height, grid_size)

# Keyboard bindings
screen.listen()
screen.onkey(lambda: snake.change_direction("Up"), "Up")
screen.onkey(lambda: snake.change_direction("Down"), "Down")
screen.onkey(lambda: snake.change_direction("Left"), "Left")
screen.onkey(lambda: snake.change_direction("Right"), "Right")

# Score
score = 0

def get_high_score():
    """Reads the highest score from the score file."""
    try:
        with open(score_file, "r") as f:
            high_score = int(f.read())
    except FileNotFoundError:
        high_score = 0
    except ValueError:
        high_score = 0 
    return high_score

def save_high_score(current_score):
    """
    Writes the current score to the score file if it's higher than the existing high score.
    """
    high_score = get_high_score()
    if current_score > high_score:
        with open(score_file, "w") as f:
            f.write(str(current_score))

high_score = get_high_score()

# Score display
score_turtle = turtle.Turtle()
score_turtle.speed(0)
score_turtle.color("white")
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(0, (screen_height / 2) - 30)
score_turtle.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

def game_loop():
    global score
    global high_score

    while True:
        screen.update()

        if snake.head.distance(food) < grid_size:
            food.move()
            snake.grow()
            score += 1
            score_turtle.clear()
            score_turtle.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

        if snake.check_collision(screen_width, screen_height):
            time.sleep(1)
            save_high_score(score) 
            high_score = get_high_score()
            snake.reset()
            food.move()
            score = 0
            score_turtle.clear()
            score_turtle.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

        snake.move()
        time.sleep(game_speed)

if __name__ == "__main__":
    game_loop()

screen.mainloop()