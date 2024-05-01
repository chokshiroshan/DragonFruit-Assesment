# Importing libraries
import random
from PIL import Image, ImageDraw
import math

# Creating a base image


def create_base_image(resolution=(1000000, 1000000)):
    '''
    Input: resolution of the image
    Output: a white image of the given resolution
    '''
    image = Image.new('1', (resolution), color='white')
    return image

# Saving the image


def save_image(image, filename):
    '''
    Input: image and filename
    Output: saves the image to the given filename
    '''
    image.save(filename, compression='tiff_deflate')

# Creating a microscope image of a parasite


def create_microscope_image(image):
    '''
    Input: image
    Output: image with a black blob in it
    '''
    draw = ImageDraw.Draw(image)
    area_of_image = image.size[0] * image.size[1]
    area_of_blob = random.randint(0.25 * area_of_image, 0.35 * area_of_image)
    print("Parasite covers: ", str(
        (area_of_blob/area_of_image)*100)[:5], "%" + " of the image")
    radius = int((area_of_blob / 3.14) ** 0.5)
    x = random.randint(radius, image.size[0] - radius)
    y = random.randint(radius, image.size[1] - radius)
    draw.ellipse((x - radius, y - radius, x +
                 radius, y + radius), fill='black')
    for angle in range(361):
        x_a = radius * math.cos(angle) + x
        y_a = radius * math.sin(angle) + y
        r = random.randint(10,100)
        draw.ellipse((x_a - (radius/r), y_a - (radius/r), x_a +
                 (radius/r), y_a + (radius/r)), fill='black')
    
    return image, x, y, radius

# Creating a dye image


def create_dye_image(image, x, y, radius, size):
    '''
    Input: image, x, y, radius
    Output: image with black dots in it
    '''
    draw = ImageDraw.Draw(image)
    number_of_dots = random.randint(10000, 30000)
    # As per document 0.1% of blobs are cancerous so I will randomly select 1 blob to be cancerous and add more dots to it.
    is_blob_cancerous = random.randint(0, 1000)

    r1,r2 = 50000,100000
    # is_blob_cancerous = 1
    # if size == 1000000:
    #     r1,r2 = 10000000,50000000
    if size == 10000:
        r1,r2 = 5000000,10000000
    if is_blob_cancerous == 1:
        number_of_dots = random.randint(r1, r2)
    for i in range(number_of_dots):
        x_dot = random.randint(x - radius, x + radius)
        y_dot = random.randint(y - radius, y + radius)
        if math.sqrt((x_dot - x)**2 + (y_dot - y)**2) > radius:
            if random.randint(0,4):
                continue
        draw.point((x_dot, y_dot), fill='black')

    # Randomly drawing black dots outside of the blob
    number_of_dots = random.randint(100000, 200000)
    for i in range(number_of_dots):
        x_dot = random.randint(0, image.size[0])
        y_dot = random.randint(0, image.size[1])
        draw.point((x_dot, y_dot), fill='black')

    return image

# Creating a dye image with lines


def create_dye_image_with_lines(image, x, y, radius):
    '''
    Input: image, x, y, radius
    Output: image with black lines in it
    '''
    draw = ImageDraw.Draw(image)
    number_of_lines = random.randint(10, 50)
    is_blob_cancerous = random.randint(0, 1000)

    if is_blob_cancerous == 1:
        number_of_lines = random.randint(50, 100)
    for _ in range(number_of_lines):
        x1 = random.randint(x - radius, x + radius)
        y1 = random.randint(y - radius, y + radius)
        x2 = random.randint(x - radius, x + radius)
        y2 = random.randint(y - radius, y + radius)
        draw.line((x1, y1, x2, y2), fill='black', width=random.randint(5, 15))

    number_of_lines = random.randint(10, 50)
    for _ in range(number_of_lines):
        x1 = random.randint(0, image.size[0])
        y1 = random.randint(0, image.size[1])
        x2 = random.randint(0, image.size[0])
        y2 = random.randint(0, image.size[1])
        draw.line((x1, y1, x2, y2), fill='black', width=random.randint(5, 15))

    return image
