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
        height = (user_settings.width * size_image[1]) / size_image[0]
    elif user_settings.width is None:
        width = (user_settings.height * size_image[0]) / size_image[1]
    return width, height


def check_of_proportionality(width, height, size_image):
    if int(width)/int(height) == size_image[0]/size_image[1]:
        return True
    else:
        return False


def resize_image(width, height, scale, size_image, original_image):
    if width and height:
        image_resize = original_image.resize((width, height))
    else:
        image_resize = original_image.resize((int(size_image[0]*scale),
                                              int(size_image[1]*scale)))
    return image_resize


def get_finish_image_size(image_resize):
    finish_size = image_resize.size
    return finish_size


def get_filepath_to_save(user_settings, finish_size):
    if user_settings.output:
        return user_settings.output
    else:
        width = finish_size[0]
        height = finish_size[1]
        filepath, image_name = os.path.splitext(user_settings.file)
        output = '{}__{}x{}{}'.format(filepath, width, height,
                                      image_name)
        return output


def save_resize_image(image_resize, output):
    image_resize.save(output)


def check_scale(scale):
    print(scale * 5)


if __name__ == '__main__':
    user_settings = get_parser_of_command_line()
    path_to_original = user_settings.file
    size_image, original_image = get_original_image_size(path_to_original)
    width = user_settings.width
    height = user_settings.height
    scale = user_settings.scale

    if scale and height and width:
        print('You entered conflicting data!')
        print('Select the scale or the width and the height!')
        print('Try again!')
        exit()
    elif height and width:
        if check_of_proportionality(width, height, size_image) is False:
            print("The width isn't proportional to the height")
        width, height = get_proportional_size(user_settings, size_image)

    check_scale(scale)

    image_resize = resize_image(width, height, scale, size_image, original_image)
    finish_size = get_finish_image_size(image_resize)
    output = get_filepath_to_save(user_settings, finish_size)
    save_resize_image(image_resize, output)