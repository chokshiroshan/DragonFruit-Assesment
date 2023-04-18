import random
from PIL import Image, ImageDraw


def create_base_image(resolution=(1000000, 1000000)):
    image = Image.new('RGB', (resolution), color='white')
    return image


def save_image(image, filename):
    image.save(filename)


def create_microscope_image(image):
    draw = ImageDraw.Draw(image)
    area_of_image = image.size[0] * image.size[1]
    area_of_blob = random.randint(0.25 * area_of_image, 0.35 * area_of_image)
    print("blob covers: ", area_of_blob/area_of_image, "%")
    radius = int((area_of_blob / 3.14) ** 0.5)
    x = random.randint(radius, image.size[0] - radius)
    y = random.randint(radius, image.size[1] - radius)
    draw.ellipse((x - radius, y - radius, x +
                 radius, y + radius), fill='black')
    return image, x, y, radius


def create_dye_image(image, x, y, radius):
    draw = ImageDraw.Draw(image)
    number_of_dots = random.randint(1000, 5000)
    # As per document 0.1% of blobs are cancerous so I will randomly select 1 blob to be cancerous and add more dots to it.
    is_blob_cancerous = random.randint(0, 1000)
    if is_blob_cancerous == 1:
        number_of_dots = random.randint(5000, 10000)
    for i in range(number_of_dots):
        x_dot = random.randint(x - radius, x + radius)
        y_dot = random.randint(y - radius, y + radius)
        draw.point((x_dot, y_dot), fill='black')

    # Randomly drawing black dots outside of the blob
    number_of_dots = random.randint(1000, 2000)
    for i in range(number_of_dots):
        x_dot = random.randint(0, image.size[0])
        y_dot = random.randint(0, image.size[1])
        draw.point((x_dot, y_dot), fill='black')

    return image


if __name__ == "__main__":
    image = create_base_image((1000, 1000))
    image, x, y, radius = create_microscope_image(image)
    save_image(image, 'test.bmp')
    image = create_base_image((1000, 1000))
    image = create_dye_image(image, x, y, radius)
    save_image(image, 'test2.bmp')
