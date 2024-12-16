class event:
    def __init__(self, paddle):
        self.paddle = paddle

    def start_move_left(self):
        self.paddle.set_speed(-10)

    def start_move_right(self):
        self.paddle.set_speed(10)

    def stop_move(self):
        self.paddle.set_speed(0)
