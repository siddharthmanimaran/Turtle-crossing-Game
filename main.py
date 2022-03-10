import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
score=Scoreboard()

screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.cars()
    cars.move_car()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            score.game_end()
            game_is_on = False
    if player.finishing():
        player.goto_start()
        cars.speed_of_car()
        score.level_up()




screen.exitonclick()