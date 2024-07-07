import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=800, height=800)
screen.title("The Kid Crossing the Road")
screen.tracer(0)  # Turn off automatic screen updates

# Register the shape (assuming kid2.gif is in the current directory)
screen.register_shape("kid2.gif")

# Create game objects
player = Player()
player.shape("kid2.gif")  # Set the shape of the player to the registered image

car_manager = CarManager()
scoreboard = Scoreboard()

# Set up key bindings for player movement
screen.listen()
screen.onkey(player.move_forward, "w")
screen.onkey(player.move_backward, "s")
screen.onkey(player.move_left, "a")
screen.onkey(player.move_right, "d")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Pause the loop for a short period
    screen.update()  # Update the screen with the new positions of objects

    car_manager.create_cars()  # Possibly create new cars
    car_manager.move_cars()    # Move all the cars on the screen

    # Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # If a car is too close to the player
            game_is_on = False
            scoreboard.game_over()  # Display game over message

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()  # Move player back to the start position
        car_manager.level_up()  # Increase the speed of the cars
        scoreboard.increase_level()  # Update scoreboard after leveling up

# Exit the game when the screen is clicked
screen.exitonclick()
