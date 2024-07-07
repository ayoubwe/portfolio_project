from turtle import Turtle

# Define constants for the player's starting position, move distance, and finish line position
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()  # Lift the pen so the turtle doesn't draw when moving
        self.go_to_start()  # Place the player at the starting position
        self.setheading(90)  # Set the initial direction of the player to face upwards

    def move_forward(self):
        # Move the player forward by the defined move distance
        self.setheading(90)  # Ensure the player is facing upwards
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        # Move the player backward by the defined move distance
        self.setheading(270)  # Ensure the player is facing downwards
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        # Move the player left by the defined move distance
        self.setheading(180)  # Ensure the player is facing left
        self.forward(MOVE_DISTANCE)

    def move_right(self):
        # Move the player right by the defined move distance
        self.setheading(0)  # Ensure the player is facing right
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        # Move the player to the starting position
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        # Check if the player has reached or crossed the finish line
        return self.ycor() > FINISH_LINE_Y
