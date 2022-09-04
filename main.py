from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from score import Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.title("My Snake Game")
screen.bgcolor('black')
screen.tracer(0)
screen.listen()


#snake creation
snake_obj=Snake()
food=Food()
score=Scoreboard()
screen.onkey(snake_obj.up,'Up')
screen.onkey(snake_obj.down,'Down')
screen.onkey(snake_obj.left,'Left')
screen.onkey(snake_obj.right,'Right')
game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake_obj.move_snake()
    if snake_obj.head.distance(food)<15:
        snake_obj.extend()
        food.refresh()
        score.increase()
    if snake_obj.head.xcor()>280 or snake_obj.head.xcor()<-280 or snake_obj.head.ycor()>280 or snake_obj.head.ycor()<-280:
        game_is_on=False
        score.game_over()

    for seg in snake_obj.snake_segments:
        if snake_obj.head == seg:
            pass
        elif snake_obj.head.distance(seg)<10:
            game_is_on=False
            score.game_over()

















screen.exitonclick()
