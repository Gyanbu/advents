from PIL import Image


def covert(array):
    x_len = len(array[0])
    y_len = len(array)
    image = Image.new('1', (x_len, y_len))
    pixels = image.load()

    for y in range(y_len):
        for x in range(x_len):
            pixels[x, y] = int(array[y][x])
    return image
