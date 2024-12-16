import turtle

class paddle:
    def __init__(self):
        self.rim = turtle.Turtle()
        self.rim.penup()
        self.rim.speed(0)
        self.rim.goto(0, -250)
        self.rim.color("orange")
        self.rim.shape("square")
        self.rim.shapesize(stretch_wid=0.5, stretch_len=6)

        self.net = turtle.Turtle()
        self.net.penup()
        self.net.speed(0)
        self.net.goto(0, -275)
        self.net.color("brown")
        self.net.hideturtle()
        self.draw_net()
        self.speed = 0

    def draw_net(self):
        self.net.clear()
        self.net.penup()
        start_x = self.rim.xcor() - 60
        self.net.goto(start_x, -250)
        self.net.pendown()
        for i in range(5):
            self.net.goto(start_x + i * 30, -250)
            self.net.goto(start_x + i * 30, -300)
            self.net.penup()
            self.net.goto(start_x + (i + 1) * 30, -250)
            self.net.pendown()
        self.net.penup()
        self.net.goto(start_x, -275)
        self.net.pendown()
        for i in range(2):
            self.net.goto(start_x + 120, -275 - i * 12)
            self.net.penup()
            self.net.goto(start_x, -275 - (i + 1) * 12)
            self.net.pendown()

    def move(self):
        new_x = self.rim.xcor() + self.speed
        if -350 <= new_x <= 350:
            self.rim.setx(new_x)
            self.net.setx(new_x)
            self.draw_net()

    def set_speed(self, speed):
        self.speed = speed
