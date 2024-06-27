import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=800)
screen.title("The Kid Crossing the Road")
screen.tracer(0)

# Register the shape (assuming kid2.gif is in the current directory)
screen.register_shape("kid2.gif")

# Create game objects
player = Player()
player.shape("kid2.gif")

car_manager = CarManager()
scoreboard = Scoreboard()

# Set up key bindings
screen.listen()
screen.onkey(player.move_forward, "w")
screen.onkey(player.move_backward, "s")
screen.onkey(player.move_left, "a")
screen.onkey(player.move_right, "d")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()  # Update scoreboard after leveling up

# Exit on click
screen.exitonclick()
