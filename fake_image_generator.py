import random
from PIL import Image, ImageDraw


def create_base_image(resolution=(1000000, 1000000)):
    img = Image.new('RGB', (resolution), color='white')
    return img


def save_image(img, filename):
    img.save(filename)


def create_circle_blob(img):
    draw = ImageDraw.Draw(img)
    area_of_image = img.size[0] * img.size[1]
    area_of_blob = random.randint(0.25 * area_of_image, 0.35 * area_of_image)
    print("blob covers: ", area_of_blob/area_of_image, "%")
    radius = int((area_of_blob / 3.14) ** 0.5)
    x = random.randint(radius, img.size[0] - radius)
    y = random.randint(radius, img.size[1] - radius)
    draw.ellipse((x - radius, y - radius, x +
                 radius, y + radius), fill='black')
    return img


if __name__ == "__main__":
    img = create_base_image((1000, 1000))
    img = create_circle_blob(img)
    save_image(img, 'test.png')
