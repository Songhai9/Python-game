import turtle

class Brick(turtle.Turtle):
    def __init__(self, position, hits=1):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.hits_left = hits
        self.update_color()
        self.goto(position)

    def update_color(self):
        """
        Update the color of the brick based on the number of hits left
        Color depends on hits_left: the greener, the more hits left
        """
        if self.hits_left == 3:
            self.color("#006400")
        elif self.hits_left == 2:
            self.color("#32CD32")
        else:
            self.color("#90EE90")

    def hit(self):
        """Reduce the number of hits left by 1."""
        self.hits_left -= 1
        if self.hits_left > 0:
            self.update_color()
        else:
            self.hide_brick()

    def hide_brick(self):
        """Hide the brick off-screen."""
        self.goto(2000, 2000)  # Move off-screen
        self.hideturtle()
