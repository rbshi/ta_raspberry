# Pong Server

import socket
from time import sleep
from sense_hat import SenseHat


############### socket preparation ###################

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('', 3542)
sock.bind(server_address)
sock.listen(1)
print("Server is listening at port 3542...")
conn, addr = sock.accept()

######################################################


sense = SenseHat()

# y is the current position of the player's bat
# opponent is the current position of the opponent's bat
# ball_position tells the current position of the ball
# ball_velocity tells the speed/direction of the ball in two dimension 
y = 4
opponent = 4
ball_position = [3, 3]
ball_velocity = [1, 1]

# method to draw the bats of both players
def draw_bat():
    sense.set_pixel(0, y, 0, 255, 0)
    sense.set_pixel(0, y + 1, 0, 255, 0)
    sense.set_pixel(0, y - 1, 0, 255, 0)
    sense.set_pixel(7, opponent, 0, 0, 255)
    sense.set_pixel(7, opponent + 1, 0, 0, 255)
    sense.set_pixel(7, opponent - 1, 0, 0, 255)

# the bat position should be updated when the joystick is pressed
def move_up(event):
    global y
    if y > 1 and event.action=='pressed':
        y -= 1

# the bat position should be updated when the joystick is pressed
def move_down(event):
    global y
    if y < 6 and event.action=='pressed':
        y += 1

# draw the ball and also update the position of the ball
def draw_ball():
    global ball_position, opponent
    # Draws the ball pixel
    sense.set_pixel(ball_position[0], ball_position[1], 255, 255, 255)
    # Moves the ball to the next position
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    if ball_position[0] == 6 and opponent - 1 <= ball_position[1] <= opponent + 1:
        ball_velocity[0] = -ball_velocity[0]
    if ball_position[1] == 0 or ball_position[1] == 7:
        ball_velocity[1] = -ball_velocity[1]
    if ball_position[0] == 0 or ball_position[0] == 7:
        ball_velocity[0] = -ball_velocity[0]
    if ball_position[0] == 1 and y - 1 <= ball_position[1] <= y + 1:
        ball_velocity[0] = -ball_velocity[0]


# specify what actions to take when the joystick events occur
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down

counter = 0

# keep running the game forever
while True:
    conn.send(("%d,%d,%d" % (y, ball_position[0], ball_position[1])).encode("utf-8"))
    incoming_y = conn.recv(1024)
    if incoming_y:
        opponent_new = int(incoming_y.decode("utf-8"))
        if 0 <= opponent_new <= 7:
            opponent = opponent_new

    if counter >= 5:
        sense.clear(0, 0, 0)
        draw_bat()
        draw_ball()
        counter = 0
    else:
        counter += 1

    sleep(0.05)
