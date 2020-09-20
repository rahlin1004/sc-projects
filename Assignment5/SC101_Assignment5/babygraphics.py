"""
Name: Sarah
=========================================================
SC101P Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000  # width of canvas
CANVAS_HEIGHT = 600  # height of canvas
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]  # the years
GRAPH_MARGIN_SIZE = 20  # the line and edge distance
COLORS = ['red', 'purple', 'green', 'blue']  # the color of the line
TEXT_DX = 2  # the word and line distance
LINE_WIDTH = 2  # the line width
MAX_RANK = 1000  # the lowest rank


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    return year_index * (width-GRAPH_MARGIN_SIZE*2) // len(YEARS) + GRAPH_MARGIN_SIZE


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas
    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # create up line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)  # create down line
    for year in range(len(YEARS)):  # make the line of the year
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year), 0, get_x_coordinate(CANVAS_WIDTH, year), CANVAS_HEIGHT)
        # year line
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=YEARS[year], anchor=tkinter.NW)  # year
    ##################################


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    color = 0  # COLORS index==0
    for name in lookup_names:  # make names
        for year in range(len(YEARS)-1):  # the different years
            if str(YEARS[year]) in name_data[name]:  # see year is in the name_data
                x1 = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/1000*int(name_data[name][str(YEARS[year])]) + \
                        GRAPH_MARGIN_SIZE  # set x1
                word = str(name_data[name][str(YEARS[year])])  # set the word
            else:
                word = '*'  # set the word *
                x1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE  # set x1
            if str(YEARS[year+1]) in name_data[name]:  # set x2
                x2 = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/1000*int(name_data[name][str(YEARS[year+1])]) + \
                     GRAPH_MARGIN_SIZE  # set x2
            else:
                x2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE  # set x2
            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year), x1, get_x_coordinate(CANVAS_WIDTH, year + 1), x2,
                               fill=COLORS[color], width=LINE_WIDTH)  # create a line
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year)+TEXT_DX, x1, text=name + '' + word,
                               anchor=tkinter.SW, fill=COLORS[color])  # create a text
        #  ===================================add the last word================================================== #
        if str(YEARS[len(YEARS)-1]) in name_data[name]:
            word = str(name_data[name][str(YEARS[len(YEARS)-1])])
            x1 = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / 1000 * int(
                name_data[name][str(YEARS[len(YEARS)-1])]) + GRAPH_MARGIN_SIZE
        else:
            word = '*'
            x1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH+TEXT_DX, len(YEARS)-1), x1, text=name + '' + word,
                           anchor=tkinter.SW, fill=COLORS[color])
        # ====================================================================================================== #
        if color == len(COLORS)-1:
            color = 0
        else:
            color += 1

# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
