# EVENT LISTENERS & TURTLE RACING CODE
from turtle import Turtle, Screen # turtle - module, Turtle,Screen - Class
import random

is_race_on =False
screen = Screen()
screen.setup(width=600,height=400)
user_bet=screen.textinput(title="Who will be the winner?",prompt="Enter the colour: ")

colors = ["red","orange","yellow","green","blue","purple"]
y_axis = [-60,-30,0,30,60]
all_turtles = []

for i in range(0,5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i]) 
    new_turtle.penup()
    new_turtle.goto(x=-280,y=y_axis[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 280:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
                break

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        















'''def move_forwards():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def move_counter_clockwise():
    tim.right(120)

def move_clockwise():
    tim.left(120)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
'''# here listen,onKey,exitonclick are higher order function defined inside Screen class, rest - move_forward is also a function
#screen.listen()
#screen.onkey(key="space",fun=move_Forwards) 
#when space is clicked the function is triggered - like passing one function into another (w/o paranthesis)
'''
screen.listen()
screen.onkey(key="W",fun=move_forwards)
screen.onkey(key="S",fun=move_backward)
screen.onkey(key="A",fun=move_counter_clockwise)
screen.onkey(key="D",fun=move_clockwise)
screen.onkey(key="C",fun=clear_screen)
'''


screen.exitonclick()