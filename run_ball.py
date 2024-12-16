import turtle
from paddle import paddle
from ball import ball
from my_event import event
import random

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")
screen.title("Ball Collector Game")
screen.tracer(0)

paddle = paddle()
event_manager = event(paddle)
ball_manager = ball()

score = 0
score_display = turtle.Turtle()
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(-350, 260)
score_display.write(f"Score: {score}", font=("Courier", 24, "normal"))

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", font=("Courier", 24, "normal"))

def show_loss_message():
    loss_message = turtle.Turtle()
    loss_message.color("red")
    loss_message.penup()
    loss_message.hideturtle()
    loss_message.goto(0, 0)
    loss_message.write("GAME OVER", align="center", font=("Arial", 36, "bold"))

screen.listen()
screen.onkeypress(event_manager.start_move_left, "Left")
screen.onkeypress(event_manager.start_move_right, "Right")
screen.onkeyrelease(event_manager.stop_move, "Left")
screen.onkeyrelease(event_manager.stop_move, "Right")

game_over = False
while not game_over:
    screen.update()
    paddle.move()
    if random.random() < 0.02:
        ball_manager.create_ball()
    for falling_ball in ball_manager.balls:
        falling_ball.sety(falling_ball.ycor() + falling_ball.dy)
        if falling_ball.ycor() < -290:
            falling_ball.goto(random.randint(-350, 350), 250)
        if (paddle.rim.ycor() - 10 < falling_ball.ycor() < paddle.rim.ycor() + 10 and
            paddle.rim.xcor() - 50 < falling_ball.xcor() < paddle.rim.xcor() + 50):
            if falling_ball.color()[0] == "red":
                game_over = True
                show_loss_message()
                break
            elif falling_ball.color()[0] == "green":
                score += 1
            elif falling_ball.color()[0] == "brown":
                score += 2
            elif falling_ball.color()[0] == "yellow":
                score += 3
            elif falling_ball.color()[0] == "blue":
                score += 4
            elif falling_ball.color()[0] == "black":
                score += 5
            update_score()
            falling_ball.goto(random.randint(-350, 350), 250)

screen.mainloop()
