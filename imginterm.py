#!/usr/bin/env python3
import argparse, shutil

from PIL import Image


# Set parser
parser = argparse.ArgumentParser()
parser.add_argument('image')
args = parser.parse_args()

# Get terminal size
termsize = shutil.get_terminal_size()

# Extraction RGB data
image = Image.open(args.image)
image.thumbnail(termsize)
rgb_image = image.convert('RGB')

# Drawing RGB image in terminal
print("x =", rgb_image.size[0], ", y =", rgb_image.size[1])
for y in range(rgb_image.size[1]):
    for x in range(rgb_image.size[0]):
        r, g, b = rgb_image.getpixel((x, y))
        print("\033[48;2;{};{};{}m  ".format(r, g, b), end='')
    print()
