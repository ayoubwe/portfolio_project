from turtle import Turtle

# Define the font style for the scoreboard
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1  # Initialize the level to 1
        self.penup()  # Lift the pen so the turtle doesn't draw when moving
        self.hideturtle()  # Hide the turtle icon
        self.goto(-280, 260)  # Position the scoreboard on the screen
        self.update_scoreboard()  # Display the initial scoreboard

    def update_scoreboard(self):
        # Clear the previous text and write the current level on the screen
        self.clear()  # Clear previous text
        self.write(f"Level: {self.level}", align="left", font=FONT)  # Display the current level

    def increase_level(self):
        # Increase the level by 1 and update the scoreboard
        self.level += 1  # Increment the level
        self.update_scoreboard()  # Update the displayed level

    def game_over(self):
        # Display the "GAME OVER" message at the center of the screen
        self.goto(0, 0)  # Move to the center of the screen
        self.write("GAME OVER", align="center", font=FONT)  # Display the game over message
