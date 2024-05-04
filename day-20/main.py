from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME 🐍")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

# PART 1 - CREATE & MOVE THE SNAKE
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detection of collision with food
    if snake.head.distance(food) < 15:
        print("Colloided ( -  - )")
        food.refresh()
        snake.extend()
        score.increase_score()
        

    #detection of collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        print("COLLOIDED...NOOO...GAME OVER")
        score.game_over()
        game_is_on = False


    #detection of collision with tail / any segment in the snake body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

        
        

    
    
        
        








screen.exitonclick()