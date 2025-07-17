import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
player = Player()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
        
    for car_instance in car.all_cars:
        if player.distance(car_instance) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.is_at_finish_line():
        player.reset_position()
        car.increase_speed()
        scoreboard.increase_level()
screen.exitonclick()    
            
    

