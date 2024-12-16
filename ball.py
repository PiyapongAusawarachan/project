import turtle
import random
import math

class ballfall(turtle.Turtle):
    def __init__(self, ball_type, x_position, y_position):
        super().__init__()
        self.penup()
        self.goto(x_position, y_position)
        self.dy = -3.3
        self.create_ball(ball_type)

    def create_ball(self, ball_type):
        self.shape("circle")
        if ball_type == "green":
            self.color("green")
            self.shapesize(2)
        elif ball_type == "brown":
            self.color("brown")
            self.shapesize(2)
        elif ball_type == "yellow":
            self.color("yellow")
            self.shapesize(1.5)
        elif ball_type == "blue":
            self.color("blue")
            self.shapesize(1.5)
        elif ball_type == "black":
            self.color("black")
            self.shapesize(1.5)
        elif ball_type == "red":
            self.color("red")
            self.shapesize(4)

class ball:
    def __init__(self):
        self.balls = []

    def create_ball(self):
        ball_type = random.choice(["green", "brown", "yellow", "blue", "black", "red"])
        x_position = random.randint(-350, 350)
        y_position = random.randint(200, 300)
        while any(math.sqrt((x_position - b.xcor())**2 + (y_position - b.ycor())**2) < 50 for b in self.balls):
            x_position = random.randint(-350, 350)
            y_position = random.randint(200, 300)
        new_ball = ballfall(ball_type, x_position, y_position)
        self.balls.append(new_ball)

    def move_balls(self):
        for ball in self.balls:
            ball.sety(ball.ycor() + ball.dy)
            if ball.ycor() < -290:
                ball.goto(random.randint(-350, 350), 250)
