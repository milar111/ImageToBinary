from io import BytesIO
from PIL import Image

def image_to_byte_array(image_path, x, y):
    im = Image.open(image_path).convert('1')
    im_resize = im.resize((x, y))
    buf = BytesIO()
    im_resize.save(buf, 'ppm')
    byte_im = buf.getvalue()
    temp = len(str(x) + ' ' + str(y)) + 4
    return byte_im[temp::]

image_path = "path\\to\\image" #when placing the path to your image use '\\' instead of '\'
x = 32  # Specify the width of the image that will be displayed (not the display resolution)
y = 32  # Specify the height of the image that will be displayed (not the display resolution)

byte_array = image_to_byte_array(image_path, x, y)
print(byte_array)

#before running the programm read the README file