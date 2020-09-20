"""
Name: Sarah
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    """
    this project plays breakout
    """
    global NUM_LIVES
    graphics = BreakoutGraphics()
    score = 0  # the score you have
    score2 = 0
    delay = 0  # the speed you have
    win = 1000
    # Add animation loop here!
    while NUM_LIVES > 0:  # if your lives > 0 you die
        if graphics.get_game_state():  # if true ( you are playing the game now )
            dx = graphics.get_dx()  # get dx
            dy = graphics.get_dy()  # get dy
            NUM_LIVES, score, delay, score2, win = graphics.bounce_ball(dx, dy, NUM_LIVES, score, delay, score2)  # bouncing the ball
        pause(FRAME_RATE + delay + 20)  # the speed of ball bouncing
        if score2 == win:  # if you break all of the bricks
            break
    graphics.remove_all(score)  # show you win or lose



if __name__ == '__main__':
    main()
