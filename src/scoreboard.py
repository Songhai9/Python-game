import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self, text_color="black"):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.color(text_color)
        self.penup()
        self.hideturtle()
        self.goto(-350, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}  Lives: {self.lives}",
            align="left",
            font=("Courier", 18, "normal"),
        )

    def increase_score(self):
        self.score += 10
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def reset(self):
        """Reset the scoreboard for a new game."""
        self.score = 0
        self.lives = 3
        self.update_scoreboard()

    def game_over(self):
        """Display game over message."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 36, "normal"))

    def win_message(self):
        """Display win message."""
        self.goto(0, 0)
        self.write("YOU WIN!", align="center", font=("Courier", 36, "normal"))
