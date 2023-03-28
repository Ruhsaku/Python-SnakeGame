from turtle import Turtle

TEXT_X_POSITION = 0
TEXT_Y_POSITION = 260
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=TEXT_X_POSITION, y=TEXT_Y_POSITION)
        self.write(f"Score {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

