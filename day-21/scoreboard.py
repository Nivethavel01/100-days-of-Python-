from turtle import Turtle


FONT = ('Courier', 24, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.l_points = 0
        self.r_points = 0
        self.goto(-20,270)
        self.hideturtle()
        self.update_score()
        

    def update_score(self):
        self.write(f"{self.l_points} ", move=False, align="left", font=FONT)
        self.write(f"{self.r_points} ", move=False, align="right", font=FONT)

    def increase_score_l(self):
        self.l_points += 1
        self.clear()
        self.update_score()

    def increase_score_r(self):
        self.r_points += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", move=False, align="centre", font=FONT)
