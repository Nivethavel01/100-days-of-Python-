from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.points=0
        self.goto(-20,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.points} ", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.points += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", move=False, align=ALIGNMENT, font=FONT)

    
         
        
