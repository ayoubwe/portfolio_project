from turtle import Turtle
import random

# Define constants for car properties and movement
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        # Initialize the list to store all car objects and set the initial speed
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        # Randomly decide whether to create a new car (1 in 6 chance)
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            # Create a new car object, configure its appearance, and add it to the list
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        # Move each car in the list backwards by the current speed
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        # Increase the speed of the cars for the next level
        self.car_speed += MOVE_INCREMENT
