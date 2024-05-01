# Importing Libraries
from PIL import Image, ImageDraw
import numpy as np

# Naive Approach to find overlap between microscope image and dye image


def find_overlap_slow(microscope_image, dye_image):
    '''
    Input: microscope_image, dye_image
    Output: microscope_black_pixels, overlaped_black_pixels
    '''
    mcount = 0
    count = 0
    for row in range(microscope_image.shape[0]):
        for col in range(microscope_image.shape[1]):
            if microscope_image[row][col] == 0:
                mcount += 1
                if dye_image[row][col] == 0:
                    count += 1
    return mcount, count
