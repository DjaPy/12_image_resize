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


def get_proportional_size(size_image, width, height):
    if height == None:
        height = (width * size_image[1]) / size_image[0]
    elif width == None:
        width = (height * size_image[0]) / size_image[1]
    return width, height


def check_of_proportionality(width, height, size_image):
    if int(width)/int(height) == size_image[0]/size_image[1]:
        return True
    else:
        return False


def resize_image(output,
                 size_image,
                 width,
                 height,
                 original_image):
    if width or height:
        image_resize = original_image.resize((width, height))
    else:
        image_resize = original_image.resize((int(size_image[0]*scale), int(size_image[1]*scale)))

    image_resize.save(output + '.jpg')
    return image_resize


if __name__ == '__main__':
    args = get_parser_of_command_line()
    path_to_original = args.file
    size_image, original_image = get_original_image_size(path_to_original)
    print(size_image[0], size_image[1])
    width = args.width
    height = args.height
    scale = args.scale
    output = args.output
    if output is None:
        output = os.path
    print(get_original_image_size(path_to_original))
    print(scale, height, width, output)
    if scale and height and width:
        print('You entered conflicting data!')
        print('Select the scale or the width and the height!')
        print('Try again!')
        exit()
    elif height and width:
        if check_of_proportionality(width, height, size_image) is False:
            print("The width isn't proportional to the height")
    elif height or width:
        width, height = get_proportional_size(size_image, width, height)

    resize_image(output, size_image, height, width, original_image)