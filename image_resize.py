from PIL import Image


def get_original_image_size(path_to_original):
    original_image = Image.open(path_to_original)
    size_image = original_image.size
    return size_image


def get_proportional_size(size_image, width=None, height=None):
    if height is None:
        height = (width * size_image[1]) / size_image[0]
    elif width is None:
        width = (height * size_image[0]) / size_image[1]
    return width, height


def resize_image(path_to_original, path_to_result):
    if width or height in ()
    image_resize = get_original_image_size(path_to_original).resize()


if __name__ == '__main__':
    path_to_original = input('Enter the path for the image: ')
    width = int(input('Enter the width of the final image: '))
    height = int(input('Enter the height of the final image: '))
    scale = int(input('Specify the scale of the final image: '))
    path_to_result = input('Specify the path to the final file: ')
