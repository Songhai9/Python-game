import turtle
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard

# Function to reset the game
def reset_game():
    global game_is_on, game_over_message
    if not game_is_on:  
        scoreboard.reset()  
        ball.reset_position() 
        paddle.goto(0, -250)  

        # Clear existing bricks
        for brick in bricks:
            brick.hideturtle()

        # Recreate bricks
        bricks.clear()
        for row in range(rows):
            for col in range(columns):
                x = start_x + col * (brick_width + padding)
                y = start_y - row * (brick_height + padding)
                if row < 2:
                    hits = 3
                elif row < 4:
                    hits = 2
                else:
                    hits = 1
                brick = Brick(position=(x, y), hits=hits)
                bricks.append(brick)

        game_over_message.clear()

        game_is_on = True

# Function to end the game and display a restart message
def end_game(message):
    global game_is_on, game_over_message
    game_is_on = False
    game_over_message.goto(0, 0)
    game_over_message.write(
        f"{message}\nPress 'R' to Restart",
        align="center",
        font=("Courier", 24, "normal")
    )

# Screen setup
screen = turtle.Screen()
screen.title("Breakout Clone - Fixed Restart")
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the paddle
paddle = Paddle((0, -250), paddle_color="black")

# Create the ball
ball = Ball(ball_color="black")

# Brick variables
bricks = []
rows = 5
columns = 10
start_x = -350
start_y = 200
brick_width = 70
brick_height = 20
padding = 5

# Create bricks
for row in range(rows):
    for col in range(columns):
        x = start_x + col * (brick_width + padding)
        y = start_y - row * (brick_height + padding)
        if row < 2:
            hits = 3
        elif row < 4:
            hits = 2
        else:
            hits = 1
        brick = Brick(position=(x, y), hits=hits)
        bricks.append(brick)

# Create scoreboard
scoreboard = Scoreboard(text_color="black")

# Create game-over message turtle
game_over_message = turtle.Turtle()
game_over_message.color("black")
game_over_message.penup()
game_over_message.hideturtle()

# Keyboard controls
screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(reset_game, "r")

game_is_on = True

# Main game loop
while True:  
    while game_is_on:
        screen.update()
        ball.move()

        # Ball collision with walls
        if ball.xcor() > 380:
            ball.setx(380)
            ball.bounce_x()

        if ball.xcor() < -380:
            ball.setx(-380)
            ball.bounce_x()

        if ball.ycor() > 280:
            ball.sety(280)
            ball.bounce_y()

        # Ball collision with paddle
        if (ball.ycor() < -230 and ball.ycor() > -240) and \
           (paddle.xcor() - 60 < ball.xcor() < paddle.xcor() + 60):
            ball.sety(-230)
            ball.bounce_y()

        # Ball below paddle -> lose a life
        if ball.ycor() < -290:
            scoreboard.lose_life()
            if scoreboard.lives == 0:
                end_game("Game Over")
            else:
                ball.reset_position()

        # Check collisions with bricks
        for brick in bricks:
            if brick.isvisible() and ball.detect_collision(brick):
                brick.hit()
                scoreboard.increase_score()
                # Check if all bricks are cleared
                if all(not b.isvisible() for b in bricks):
                    end_game("You Win!")
                break  # Exit loop to handle one collision per frame

    screen.update()
