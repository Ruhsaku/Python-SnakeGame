from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Create and modify the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)

# Create the objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Create a movement
screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right")

# Variables
game_is_on = True
collision_wall_distance = 15
collision_tail_distance = 10
wall_border = 290


while game_is_on:
    screen.update()  # Updates the screen when the for loop is over
    time.sleep(0.1)  # Add a delay in the movement
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < collision_wall_distance:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with food
    if snake.head.xcor() > wall_border or snake.head.xcor() < -wall_border or\
            snake.head.ycor() > wall_border or snake.head.ycor() < -wall_border:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < collision_tail_distance:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
