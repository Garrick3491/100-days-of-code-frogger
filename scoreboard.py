from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def next_level(self):
        self.level += 1
        self.update_score_board()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)