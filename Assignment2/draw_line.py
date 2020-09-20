"""
File: draw_line.py
Name: Sarah Lin
-------------------------
this program help you to draw lines
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
SIZE = 10  # this constant control the circle size
w = GWindow(500, 500, title='drawing_line.py')  # window
TIME = 0  # this constant control the time you click
circle = GOval(SIZE, SIZE)  # a circle


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(event):
    """
    :param event: mouse event
    """
    global TIME
    TIME += 1
    if TIME % 2 == 1:  # if TIME is oval, add circle
        w.add(circle, x=event.x - SIZE/2, y=event.y - SIZE/2)
    else:
        line = GLine(circle.x + SIZE/2, circle.y + SIZE/2, event.x, event.y)
        w.remove(circle)
        w.add(line)


if __name__ == "__main__":
    main()
