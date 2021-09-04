import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player_turtle = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player_turtle.up, "Up")
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if car.distance(player_turtle)< 20:
            scoreboard.game_over()
            game_is_on = False

    if player_turtle.is_at_finish_line():
        player_turtle.go_to_start()
        scoreboard.next_level()
        car_manager.level_up()


screen.exitonclick()