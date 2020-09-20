"""
Name: Sarah
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.

class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        self.game_started = False
        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a  score and a live
        self.sscore = GLabel('{score}: 0')
        self.sscore.font = '-20'
        self.window.add(self.sscore, x=0, y=self.sscore.height+20)
        self.live = GLabel('3 :{live}')
        self.live.font = '-20'
        self.window.add(self.live, x=window_width - self.live.width, y=self.live.height + 20)
        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height, x=window_width//2-paddle_width//2, y=window_height - paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width // 2 - ball_radius, y=window_height // 2 - ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)
        # Default initial velocity for the ball.
        self.__dyr__dxr()
        # Initialize our mouse listeners.
        onmousemoved(self.move_paddle)
        onmouseclicked(self.start)
        # Draw bricks.
        for cols in range(brick_cols):
            for row in range(brick_rows):
                block = GRect(brick_width, brick_height)
                self.block = block
                block.filled = True
                block.color = self.block_color(cols)
                block.fill_color = self.block_color(cols)
                self.window.add(block, x=(block.width + brick_spacing)*row, y=brick_offset+(brick_spacing+block.height)*cols)
        # draw a disturb playing block
        self.brick_width = brick_width
        self.disturb = GRect(brick_width + 20, brick_height, x=self.window.width-brick_width, y=250)
        self.disturb.color = 'magenta'
        self.disturb.filled = True
        self.disturb.fill_color = 'magenta'
        self.window.add(self.disturb)
        self.d = -1
        # set self
        self.brick_c = brick_cols
        self.brick_row = brick_rows

    def __dyr__dxr(self):
        """
        set __dx and __dy
        """
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if (random.random() > 0.5):
            self.__dx = -self.__dx

    def block_color(self, c):
        """
        :param c: brick's cols
        :return: the brick's color
        """
        if int(c//2) == 0:
             return 'red'
        elif int(c//2) == 1:
            return 'orange'
        elif int(c//2) == 2:
            return 'yellow'
        elif int(c//2) == 3:
            return 'green'
        elif int(c//2) == 4:
            return 'blue'


    def move_paddle(self, event):
        """
        :param event: mouse
        """
        if not event.x < 0 + self.paddle.width //2 and not event.x + self.paddle.width // 2 > self.window.width:
            self.paddle.x = event.x - self.paddle.width // 2

    def get_dx(self):
        """
        :return __dx: the speed of the ball x
        """
        return self.__dx

    def get_dy(self):
        """
        :return  __dy: the speed of the ball y
        """
        return self.__dy

    def bounce_ball(self, dx, dy, lives, score, delay, score2):
        """
        :param dx: the speed of the ball x
        :param dy: the speed of the ball y
        :param lives: the lives you left
        :param score: the score you have
        :param delay: the pause time
        :return lives, score, delay: the lives , score, pause time
        """
        self.disturb.x += self.d
        self.d -= 1
        if self.disturb.x <= 0:
            self.d = -self.d
        elif self.disturb.x > self.window.width-self.disturb.width:
            self.disturb.x = self.window.width-self.brick_width-50
            self.d = -1
        # bounce at the edge
        if self.ball.x + self.ball.width > self.window.width or self.ball.x < 0:  # x
            if self.ball.y + self.ball.width > self.window.height or self.ball.y < 0:  # if the ball bounce at the corner
                dx *= -1
                dy *= -1
            else:
                dx *= -1
        elif self.ball.y < 0:  # y
            if self.ball.x + self.ball.width > self.window.width or self.ball.x < 0:  # if the ball bounce at the corner
                dy *= -1
                dx *= -1
            else:
                dy *= -1
        elif self.ball.y + self.ball.width > self.window.height:  # if the ball bounce at the ground
            lives -= 1  # live - 1
            self.game_started = False  # the ball is not bouncing now
            self.ball.x = self.window.width // 2 - self.ball.width//2
            self.ball.y = self.window.height // 2 - self.ball.width//2
            self.__dyr__dxr()
            self.sscore.text = '{score}: ' + str(score)
            self.live.text = str(lives) + ' :{live}'
            return lives, score, delay, score2, self.brick_c*self.brick_row
        # bounce at the block
        elif self.window.get_object_at(self.ball.x, self.ball.y):
            maybe_obj = self.window.get_object_at(self.ball.x, self.ball.y)
            if self.ball.y > 50:
                if self.ball.y < 250 and self.ball.y > 49:
                    self.window.remove(maybe_obj)
                    score += self.score(maybe_obj.y)
                    score2 += 1
                    delay -= 0.2
                elif self.ball.y > 350:
                    self.ball.y = self.paddle.y - self.ball.height
                if self.ball.y > 49:
                    dy *= -1
        elif self.window.get_object_at(self.ball.x + BALL_RADIUS*2, self.ball.y):
            maybe_obj = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
            if self.ball.y > 50:
                if self.ball.y < 250 and self.ball.y > 49:
                    self.window.remove(maybe_obj)
                    score += self.score(maybe_obj.y)
                    score2 += 1
                    delay -= 0.2
                elif self.ball.y > 350:
                    self.ball.y = self.paddle.y - self.ball.height
                if self.ball.y > 49:
                    dy *= -1
        elif self.window.get_object_at(self.ball.x, self.ball.y + self.ball.width):
            maybe_obj = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.width)
            if self.ball.y > 50:
                if self.ball.y + self.ball.width < 250 and self.ball.y + self.ball.width > 49:
                    self.window.remove(maybe_obj)
                    score += self.score(maybe_obj.y)
                    score2 += 1
                    delay -= 0.2
                elif self.ball.y > 350:
                    self.ball.y = self.paddle.y - self.ball.height
                if self.ball.y > 49:
                    dy *= -1
        elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.width):
            maybe_obj = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.width)
            if self.ball.y > 50:
                if self.ball.y + self.ball.width < 250 and self.ball.y + self.ball.width > 49:
                    self.window.remove(maybe_obj)
                    score += self.score(maybe_obj.y)
                    score2 += 1
                    delay -= 0.2
                elif self.ball.y > 350:
                    self.ball.y = self.paddle.y - self.ball.height
                if self.ball.y > 49:
                    dy *= -1
        self.ball.move(dx, dy)
        self.__dx = dx
        self.__dy = dy
        self.sscore.text = '{score}: ' + str(score)
        self.live.text = str(lives)+' :{live}'
        return lives, score, delay, score2, self.brick_c*self.brick_row

    def start(self, event):
        """
        :param event: mouse
        """
        if not self.game_started:
            self.game_started = True

    def get_game_state(self):
        """
        :return game_start: is the game running?
        """
        return self.game_started

    def score(self, y):
        if y < 80:
            return 5
        elif y < 120:
            return 4
        elif y < 160:
            return 3
        elif y < 200:
            return 2
        elif y < 240:
            return 1

    def remove_all(self, score):
        self.window.remove(self.ball)
        self.window.remove(self.paddle)
        self.window.remove(self.sscore)
        self.window.remove(self.live)
        self.window.remove(self.disturb)
        if score == 300:
            win = GLabel('YOU WIN!!  .　.    YA!!!!!!!!!\n         　        Ｕ', x=50, y=350)
            win.font = '-20'
            self.window.add(win)
        else:
            sscore = GLabel('YOUR SCORE IS:' + str(score) + '\n HA HA HA YOU LOSE!!!', x=50, y=350)
            sscore.font = '-20'
            self.window.add(sscore)
