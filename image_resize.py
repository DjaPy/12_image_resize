from PIL import Image
from argparse import ArgumentParser
import os
import sys


def get_parser_of_command_line():
    parser = ArgumentParser(description='Resize image')
    parser.add_argument('path_to_file',
                        help='Image to resize path', type=str)
    parser.add_argument('-w', '--width', nargs='?',
                        help='Width of new image', default=None, type=int)
    parser.add_argument('-i', '--height', nargs='?',
                        help='Height of new image', default=None, type=int)
    parser.add_argument('-s', '--scale', nargs='?',
                        help='Scale to resize', default=None, type=float)
    parser.add_argument('-o', '--output', nargs='?',
                        help='Path to new image', default=None)
    return parser.parse_args()


def get_original_image_size(path_to_original):
    original_image = Image.open(path_to_original)
    size_image = original_image.size
    return size_image, original_image


def get_proportional_size(size_image):
    if user_settings.height is None:
        height = int((user_settings.width * size_image[1]) / size_image[0])
        width = int(user_settings.width)
    elif user_settings.width is None:
        width = int((user_settings.height * size_image[0]) / size_image[1])
        height = int(user_settings.height)
    else:
        width = user_settings.width
        height = user_settings.height
    return width, height


def check_of_proportionality(size_image):
    return int(user_settings.width)/int(user_settings.height) == size_image[0]/size_image[1]


def resize_image(size_image, original_image):
    if user_settings.width is None and user_settings.height is None:
        width = int(size_image[0] * user_settings.scale)
        height = int(size_image[1] * user_settings.scale)
    else:
        width, height = get_proportional_size(size_image)
    image_resize = original_image.resize((width, height))
    return image_resize


def check_for_validity(size_image):
    if user_settings.scale and (user_settings.height or user_settings.width):
        raise ValueError('You entered conflicting data!'
                         ' Select the scale or the width and the height!'
                         ' Try again!')
    elif user_settings.width and user_settings.height:
        if not check_of_proportionality(size_image):
            print("The width isn't proportional to the height")


def get_filepath_to_save(image_resize, path_to_file, output):
    finish_size = image_resize.size
    width, height = finish_size[0], finish_size[1]
    filepath, image_name = os.path.splitext(user_settings.path_to_file)
    output = '{}__{}x{}{}'.format(filepath, width, height, image_name)
    return output


def save_resize_image(image_resize, path_to_file, output):
    output = user_settings.output
    if output is None:
        output = get_filepath_to_save(image_resize, user_settings.path_to_file,
                                      user_settings.output)
    image_resize.save(output)


if __name__ == '__main__':
    user_settings = get_parser_of_command_line()
    size_image, original_image = get_original_image_size(user_settings.path_to_file)
    check_for_validity(size_image)
    image_resize = resize_image(size_image,original_image)
    save_resize_image(image_resize, user_settings.path_to_file,
                      user_settings.output)