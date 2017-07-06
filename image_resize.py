from PIL import Image
from argparse import ArgumentParser
import os


def get_parser_of_command_line():
    parser = ArgumentParser(description='Resize image')
    parser.add_argument('file',
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


def get_proportional_size(user_settings, size_image):
    if user_settings.height is None:
        height = int((user_settings.width * size_image[1]) / size_image[0])
        width = int(user_settings.width)
    elif user_settings.width is None:
        width = int((user_settings.height * size_image[0]) / size_image[1])
        height = int(user_settings.height)
    return width, height


def check_of_proportionality(width, height, size_image):
    return bool(int(width)/int(height) == size_image[0]/size_image[1])



def resize_image(width, height, scale, size_image, original_image,
                 user_settings):
    if width is None and height is None:
        width = int(size_image[0]*scale)
        height = int(size_image[1]*scale)
    elif width is None or height is None:
        width, height = get_proportional_size(user_settings, size_image)
    image_resize = original_image.resize((width, height))
    return image_resize


def check_for_validity(width, height, scale, size_image):
    if scale and height and width:
        print('You entered conflicting data!')
        print('Select the scale or the width and the height!')
        print('Try again!')
        exit()
    elif width and height:
        print(width, height)
        if check_of_proportionality(width, height, size_image) is False:
            print("The width isn't proportional to the height")
    else:
        print('проверка')
        return True


def get_filepath_to_save(image_resize):
    finish_size = image_resize.size
    width = finish_size[0]
    height = finish_size[1]
    filepath, image_name = os.path.splitext(user_settings.file)
    output = '{}__{}x{}{}'.format(filepath, width, height,
                                      image_name)
    return output


def save_resize_image(image_resize, user_settings):
    output = user_settings.output
    if user_settings.output is None:
        output = get_filepath_to_save(image_resize)
    image_resize.save(output)


if __name__ == '__main__':
    user_settings = get_parser_of_command_line()
    path_to_orig = user_settings.file
    size_image, original_image = get_original_image_size(path_to_orig)
    width = user_settings.width
    height = user_settings.height
    scale = user_settings.scale

    if check_for_validity(width, height, scale, size_image) is True:
        width, height = get_proportional_size(user_settings, size_image)
    image_resize = resize_image(width, height, scale, size_image,
                                original_image, user_settings)
    save_resize_image(image_resize, user_settings)