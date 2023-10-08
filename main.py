from turtle import Screen
import time
from player import Player
from car_object import Cars
from scoreboard import Scoreboard, Finish


screen = Screen()
player = Player()
scoreboard = Scoreboard()
car = Cars()
finish_line = Finish()

game_is_on = True


screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()

screen.onkey(key="w", fun=player.move_up)


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    car.cor()
    # checking for collision
    for obj in car.cars:
        if obj.distance(player) < 20:
            # reducing lives and checking if game over
            if scoreboard.n_lives == 0:
                scoreboard.game_over()
                game_is_on = False
            else:
                player.restart()
                scoreboard.reset_()
    # checking if player finished level
    if player.ycor() > 250:
        scoreboard.score_up()
        car.level += 1
        player.restart()

screen.exitonclick()
