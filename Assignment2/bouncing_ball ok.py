"""
File: bouncing_ball.py
Name: Sarah Lin
-------------------------
this program shows a circle bouncing
"""

from campy.graphics.gobjects import GOval, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 5  # this constant control the circle x move
DELAY = 100  # this constant control the speed it pause
GRAVITY = 1  # this constant control the circle y move
SIZE = 20  # this constant control the size of circle
REDUCE = 0.9  # this constant control the height each time
START_X = 30  # this constant control the circle pre x
START_Y = 90  # this constant control the circle pre y
TURN = True  # if this constant is True, the circle is not moving. if is False, the circle is moving
window = GWindow(800, 500, title='bouncing_ball.py')  # window
TIME = 0  # this constant control the times you can play
score_label = GLabel('chance:' + str(3-TIME))  # show round
circle = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    circle.filled = True
    score_label.font = '-30'
    window.add(score_label, x=10, y=score_label.height+10)
    onmouseclicked(start)


def start(event):
    """
    :param event: mouse event
    """
    global TURN
    global TIME
    if TURN and TIME != 3:
        TIME += 1
        score_label.text = 'chance:' + str(3 - TIME)
        TURN = False  # the circle is moving
        window.add(circle)
        speed_y = GRAVITY
        while circle.x + circle.width < window.width:
            while circle.y + circle.height <= window.height and circle.x + circle.width < window.width:
                circle.move(VX, speed_y)
                speed_y += GRAVITY
                pause(DELAY)
                print(speed_y)
            speed_y = -speed_y * REDUCE
            circle.y = window.height - circle.height
        TURN = True
        circle.x = START_X
        circle.y = START_Y

if __name__ == "__main__":
    main()
