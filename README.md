Game Project: Ball Collector Game

This game is a paddle and falling ball collection game built using Python's turtle module. Players control 
a basket-shaped paddle to catch balls of various colors while avoiding the red ball, which ends the game.

How the Game Works

Objective:  Collect balls of different colors to gain points.Avoid the red ball, which ends the game immediately.
Gameplay
Use the arrow keys to move the paddle:
Left Arrow: Move the paddle left.
Right Arrow: Move the paddle right.
Each ball color grants a specific number of points:

Green Ball: +1 point
Brown Ball: +2 points
Yellow Ball: +3 points
Blue Ball: +4 points
Black Ball: +5 points
Collecting a Red Ball triggers a "Game Over" screen.

Coding:
1. paddle.py
Handles the paddle creation and movement.
Class: paddle
__init__():
Initializes the paddle with two components: the rim (orange rectangle) and the net (brown net below the rim).
Sets the initial position of the paddle and the speed to 0.

draw_net():
Draws vertical and horizontal lines to form a net under the rim.  Dynamically adjusts 
its position based on the paddle's location.

move():
Updates the paddle's position horizontally based on the current speed. Prevents the paddle from moving 
outside the screen boundaries.

set_speed(speed):
Adjusts the paddle's horizontal speed.

2. ball.py
Manages the falling balls.
Class: ballfall
__init__(ball_type, x_position, y_position):
Creates a ball of a specific type (e.g., green, brown, red). Sets the ball's initial position and falling speed.

create_ball(ball_type):
Adjusts the size and color of the ball based on its type. The red ball is significantly larger for emphasis.

Class: ball
__init__():
Initializes an empty list to store all falling balls.

create_ball():
Randomly creates a new ball of a specific type and position. Ensures new balls do not overlap with existing balls.

move_balls():
Moves all balls downward and resets their position if they fall off the screen.

3. event.py
Handles player input for paddle movement.
Class: event
__init__(paddle):
Links the paddle to the event manager for movement control.

start_move_left():
Starts moving the paddle to the left by setting a negative speed.

start_move_right():
Starts moving the paddle to the right by setting a positive speed.

stop_move():
Stops the paddle's movement by resetting its speed to 0.

4. run_ball.py

The main game part.

Functions
update_score():
Clears and redraws the score display with the current score.

show_loss_message():
Displays a "Game Over" message in the center of the screen when the player collects a red ball.

Main Loop
Game Initialization: Sets up the screen, paddle, event manager, and ball manager.

Game Loop: Continuously updates the paddle's position, creates new balls, moves existing balls, and checks 
for collisions. Ends the game and displays the loss message if the red ball is collected.

How to control
Arrow Keys:
Left Arrow: Move paddle left.
Right Arrow: Move paddle right.


               

                                                                                     Piyapong Ausawarachan







