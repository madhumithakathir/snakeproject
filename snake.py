STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
Up=90
Down=270
Right=0
Left=180
from turtle import Turtle
class Snake:

    def __init__(self):
        self.snake_segments=[]
        self.create_snake()
        self.head=self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move_snake(self):

        for seg in range(len(self.snake_segments)-1,0,-1):
            x_cor=self.snake_segments[seg-1].xcor()
            y_cor=self.snake_segments[seg-1].ycor()
            self.snake_segments[seg].goto(x_cor,y_cor)
        self.head.forward(20)


    def up(self):
        if self.head.heading()!=Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)

    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)


