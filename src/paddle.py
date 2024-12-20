import turtle

class Paddle(turtle.Turtle):
    def __init__(self, position, paddle_color="black"):
        super().__init__()
        self.shape("square")
        self.color(paddle_color)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.goto(position)

    def move_left(self):
        new_x = self.xcor() - 20
        if new_x > -340:  
            self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        if new_x < 340:
            self.goto(new_x, self.ycor())
