import turtle
import random

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.reset_position()

    def reset_position(self):
        """Reset the ball position to the center of the screen."""
        self.goto(0, -200)
        self.dx = random.choice([1, -1])
        self.dy = 1

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.dx *= -1

    def bounce_y(self):
        self.dy *= -1
