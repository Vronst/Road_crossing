from turtle import Turtle
HOME_X = 0
HOME_Y = -280
MOVE = 10
FINISH = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.goto(x=HOME_X, y=HOME_Y)

    def move_up(self):
        new_y = self.ycor() + MOVE
        self.goto(self.xcor(), new_y)

    def restart(self):
        self.goto(HOME_X, HOME_Y)
