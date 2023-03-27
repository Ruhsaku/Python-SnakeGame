from turtle import Screen
from snake import Snake
from food import Food
import time

# import time

# Create and modify the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)

# Create the objects
snake = Snake()
food = Food()

# Create a movement
screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right")

# Variables
game_is_on = True
collision_distance = 15

# Create the snake


while game_is_on:
    screen.update()  # Updates the screen when the for loop is over
    time.sleep(0.1)  # Add a delay in the movement
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < collision_distance:
        food.refresh()

screen.exitonclick()
