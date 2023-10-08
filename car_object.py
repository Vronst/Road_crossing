from turtle import Turtle
import random

COLOR = ["blue", "yellow", "white", "red", "purple", "orange"]
STARTING = 5
INCREMENT = 5


class Cars:

    def __init__(self):
        self.cars = []
        self.level = 0

    def create_car(self):
        random_chance = random.randint(1, 7)
        if random_chance == 6:
            new_car = Turtle("square")
            # new_car.speed("fastest")
            new_car.color(random.choice(COLOR))
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            # new_car.spawn()
            # new_car.level = level
            new_car.goto(x=310, y=random.randint(-230, 230))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(STARTING + (self.level * INCREMENT))
            # new_x = car.xcor() - STARTING - ((self.level - 1) * INCREMENT)
            # car.goto(new_x, car.ycor())

    def cor(self):
        for car in self.cars:
            if car.xcor() < -310:
                del car

    def crash(self):
        for car in self.cars:
            x = car.xcor()
            y = car.ycor()
            cords = (x, y)
            return cords
    # def spawn(self):
    #     self.cars[].(x=310, y=random.randint(-250, 250))
