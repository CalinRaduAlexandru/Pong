from turtle import Turtle

SCORE = 0
ALIGN = "center"
SCORE_FONT = ("courier", 80, "normal")
GAMEOVER_FONT = ("arial", 32, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shapesize(stretch_len = 0.3, stretch_wid = 3)
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font=SCORE_FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGN, font=SCORE_FONT)

    def l_win(self):
        self.l_score += 1
        self.update_score()

    def r_win(self):
        self.r_score += 1
        self.update_score()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
