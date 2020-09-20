"""
Name: Sarah lin
SC101 - Assignment4
Adapted from Nick Parlante's Ghost assignment by
Jerry Liao.
-----------------------------------------------
this program let you input pictures and remove the passerby
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the square of the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): squared distance between red, green, and blue pixel values

    """
    color_distance = ((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)**0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    blue_t = 0
    red_t = 0
    green_t = 0
    for pixel in pixels:
        blue_t += pixel.red
        green_t += pixel.green
        blue_t += pixel.blue
    blue_t //= len(pixels)
    green_t //= len(pixels)
    red_t //= len(pixels)
    rgb = [red_t, green_t, blue_t]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    rgb = get_average(pixels)  # avg
    min_dist = 257  # the compare num
    
    best = pixels[0]  #
    for p in pixels:
        if get_pixel_dist(p, rgb[0], rgb[1], rgb[2]) < min_dist:
            min_dist = get_pixel_dist(p, rgb[0], rgb[1], rgb[2])
            best = p
    # best = [red, green, blue]
    return best

def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    print(1)
    pixels = []
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):  # x
        for y in range(height):  # y
            for img in images:  # the pictures pixel
                pix = img.get_pixel(x, y)
                pixels.append(pix)  # add the pixel in pixels
            best = get_best_pixel(pixels)  # choose the best pixel of all
            pixel = result.get_pixel(x, y)
            pixel.red = best.red
            pixel.green = best.green
            pixel.blue = best.blue
            pixels = []  # clear up pixels
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    """
    remove passerby
    """
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
