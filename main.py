import time
from turtle import Turtle, Screen

# import time

# Create and modify the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)

# Variables
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
game_is_on = True

# Create the snake(3 squares)
for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

while game_is_on:
    screen.update()  # Updates the screen when the for loop is over
    time.sleep(0.5)  # Add a delay in the movement

    # Move every square compared to the first
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    # segments[0].left(90)


screen.exitonclick()
