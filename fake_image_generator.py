# generate 1000x1000 white pixel image

from PIL import Image


def create_base_image():
    img = Image.new('RGB', (1000, 1000), color='white')
    img.save('base_image.png')


if __name__ == "__main__":
    create_base_image()
