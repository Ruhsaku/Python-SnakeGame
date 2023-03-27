from turtle import Turtle, Screen
from snake import Snake
import time

# import time

# Create and modify the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right")

# Variables
game_is_on = True

# Create the snake


while game_is_on:
    screen.update()  # Updates the screen when the for loop is over
    time.sleep(0.1)  # Add a delay in the movement
    snake.move()

screen.exitonclick()
