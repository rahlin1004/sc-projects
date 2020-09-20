"""
File: sierpinski.py
Name: Sarah Lin
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 10                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The legth of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow
H = 0.866                  # The height of triangle

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	this program help you draw a sierpinski triangle
	"""
	draw_first_triangle()
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: int, the times of triangle
	:param length: the triangle side_length
	:param upper_left_x: the upper_left x of the triangle
	:param upper_left_y: the upper_left y of the triangle
	:return: None
	"""
	pause(0)
	if order == 1:
		pass
	else:
		# ============================================ draw the triangle ============================================ #
		l1 = GLine(upper_left_x+length*0.5, upper_left_y, upper_left_x+length//2*0.5, upper_left_y+length//2*H)
		l2 = GLine(upper_left_x+length*0.5, upper_left_y, upper_left_x+length*0.5*1.5, upper_left_y+length//2*H)
		l3 = GLine(upper_left_x + length // 2 * 0.5, upper_left_y + length // 2 * H,
				upper_left_x + length // 2 * 0.5 * 3, upper_left_y + length // 2 * H)
		# =========================================================================================================== #
		sierpinski_triangle(order - 1, length // 2, upper_left_x, upper_left_y)
		sierpinski_triangle(order - 1, length // 2, upper_left_x + length*0.5, upper_left_y)
		sierpinski_triangle(order - 1, length // 2, upper_left_x + length*0.25, upper_left_y + length/2*H)
		window.add(l1)
		window.add(l2)
		window.add(l3)


def draw_first_triangle():
	"""
	draw the first triangle
	"""
	l1 = GLine(UPPER_LEFT_X, UPPER_LEFT_Y, UPPER_LEFT_X + LENGTH * 0.5, UPPER_LEFT_Y + LENGTH * 0.866)
	window.add(l1)
	l2 = GLine(UPPER_LEFT_X, UPPER_LEFT_Y, UPPER_LEFT_X + LENGTH * 0.5 * 2, UPPER_LEFT_Y)
	window.add(l2)
	l3 = GLine(UPPER_LEFT_X + LENGTH, UPPER_LEFT_Y, UPPER_LEFT_X + LENGTH * 0.5, UPPER_LEFT_Y + LENGTH * 0.866)
	window.add(l3)


if __name__ == '__main__':
	main()