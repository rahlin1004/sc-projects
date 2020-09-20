"""
File: my_drawing.py
Name: Sarah lin
----------------------
This program show micky to you
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    This program show micky to you
    """
    window = GWindow(width=800, height=500, title="林冠伶")
    back(window)
    up(window)
    eye(window)
    body(window)
    word(window)


def back(window):
    """
    :param window:window
    """
    blue = GRect(800, 500)
    blue.color = 'PaleTurquoise'
    blue.filled = True
    blue.fill_color = 'PaleTurquoise'
    window.add(blue)
    back = GOval(300, 300, x=100, y=50)
    back.color = 'white'
    back.filled = True
    back.fill_color = 'gray'
    window.add(back)
    back_1 = GOval(150, 150)
    back_1.color = 'gray'
    back_1.filled = True
    back_1.fill_color = 'gray'
    window.add(back_1)
    back_2 = GOval(150, 150)
    back_2.color = 'gray'
    back_2.filled = True
    back_2.fill_color = 'gray'
    window.add(back_2, x=150+200, y=0)
    neck = GRect(50, 70, x=back.width//2+70, y=300)
    neck.color = 'gray'
    neck.filled = True
    neck.fill_color = 'gray'
    window.add(neck)
    body1 = GOval(400, 300, x=50, y=360)
    body1.color = 'pink'
    body1.filled = True
    body1.fill_color = 'pink'
    window.add(body1)
    body2 = GOval(50, 100, x=150, y=400)
    body2.color = 'Light yellow'
    body2.filled = True
    body2.fill_color = 'Light yellow'
    window.add(body2)
    body3 = GOval(50, 100, x=250, y=400)
    body3.color = 'Light yellow'
    body3.filled = True
    body3.fill_color = 'Light yellow'
    window.add(body3)
    tree1 = GRect(70, 300, x=600, y=230)
    tree1.color = 'PaleGoldenrod'
    tree1.filled = True
    tree1.fill_color = 'PaleGoldenrod'
    window.add(tree1)
    tree2 = GOval(170, 170, x=550, y=150)
    tree2.color = 'Pale green'
    tree2.filled = True
    tree2.fill_color = 'Pale green'
    window.add(tree2)


def nose(window):
    """
    :param window:window
    """
    nose_up = GOval(50, 20)
    nose_up.filled = True
    window.add(nose_up, x=window.width / 2-nose_up.width//2, y=245+40)


def eye(window):
    """
    :param window:window
    """
    eye1 = GOval(30, 70, x=window.width / 2-32, y=window.height / 2-35)
    eye1.filled = True
    eye1.fill_color = "snow"
    window.add(eye1)
    eye11 = GOval(20, 40, x=window.width / 2 - 27, y=window.height / 2 -5)
    eye11.filled = True
    window.add(eye11)
    eye2 = GOval(30, 70, x=window.width-eye1.x - 23, y=window.height-eye1.y-70)
    eye2.filled = True
    eye2.fill_color = "snow"
    window.add(eye2)
    eye22 = GOval(20, 40, x=window.width-eye11.x-12, y=window.height-eye11.y-10)
    eye22.filled = True
    window.add(eye22)
    nose(window)


def word(window):
    """
    :param window:window
    """
    square = GRect(150, 30)
    square.filled = True
    square.fill_color = "Crimson"
    square.color = 'Crimson'
    window.add(square, x=window.width / 2-square.width/2, y=375)
    code = GLabel("stanCode")
    code.color = 'snow'
    code.font = "-20"
    window.add(code, x=window.width / 2-code.width/2, y=380+code.height)


def body(window):
    """
    :param window:window
    """
    x = 0
    for i in range(5):
        body_square = GRect(40, 200, x=300+x, y=300)
        body_square.filled = True
        if i % 2 != 0:
            body_square.fill_color = 'white'
        else:
            body_square.fill_color = 'red'
        window.add(body_square)
        x += 40


def up(window):
    """
    :param window: window
    """
    head = GOval(200, 200)
    head.filled = True
    window.add(head, x=window.width / 2 - head.width/2, y=window.height / 2 - head.height/2)
    ear1 = GOval(100, 100)
    ear1.filled = True
    window.add(ear1, x=head.x - ear1.width/2, y=head.y - ear1.height/2)
    ear2 = GOval(100, 100)
    ear2.filled = True
    window.add(ear2, x=head.x + (head.width-ear2.width/2), y=head.y - ear2.height/2)
    heads1 = GOval(head.width//2.5, head.height-80, x=window.width / 2 - 70, y=window.height / 2-70)
    heads1.filled = True
    window.add(heads1)
    heads1.fill_color = 'Moccasin'
    heads2 = GOval(head.width // 2.5, head.height-80, x=window.width / 2-10, y=window.height / 2 - 70)
    heads2.filled = True
    heads2.color = 'Moccasin'
    window.add(heads2)
    heads2.fill_color = 'Moccasin'
    mouth = GOval(head.width-20, 70, x=window.width / 2 - 90, y=window.height / 2+10)
    mouth.filled = True
    window.add(mouth)
    mouth.color = 'Moccasin'
    mouth.fill_color = 'Moccasin'


if __name__ == '__main__':
    main()
