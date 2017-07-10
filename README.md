# Image Resizer

The script changes the size of your image.

# HowTo

Use Venv or virtualenv for insulation project.
Virtualenv example:

```
$python virtualevn myenv
$source myenv/bin/activate
```
Install requirements:

```
pip install -r requirements.txt
```
if you have error, you need enter `sudo` before command.

## Quick launch

Example quick launch.

```
python /path/to/image_resize.py name_image.jpg -s 2
```

List of arguments:
- `-h, --help` - list of all commands;
- `-w, --width` - width of out image;
- `-i, --height` - height of out image;
- `-o, --output` - the way with name of resized image to save.
If there is no way, the file will save in the directory
with the original image. The file name will be the following - for test.jpg with
res 400x400 resized image without `-o` is test__200x200.jpg by command
`python resize_image.py test.jpg -s 2`

Availiable combinations of size arguments:

- `-s` - resize image by scale
- `-w` - resize image only by width. Proportions will be saved.
- `-i` - resize image only by height. Proportions will be saved.
- `-w -s` or `-i -s` - resize image by width and height and scale. You will get an error and text:
```
You entered conflicting data!
Select the scale or the width and the height!
Try again!
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
