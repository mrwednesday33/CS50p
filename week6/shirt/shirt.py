import sys
import os
from PIL import Image, ImageOps

# Check for the correct number of command-line arguments
if len(sys.argv) != 3:
    sys.exit("Too few or too many command-line arguments")

# Check if the input and output files have the correct extensions
in_ext = os.path.splitext(sys.argv[1])[1].lower()
out_ext = os.path.splitext(sys.argv[2])[1].lower()
if in_ext not in ('.jpg', '.jpeg', '.png') or out_ext not in ('.jpg', '.jpeg', '.png'):
    sys.exit("Invalid input or output format")

# Check if the input file exists
if not os.path.exists(sys.argv[1]):
    sys.exit("Input does not exist")

# Load the shirt image
shirt = Image.open("shirt.png")

# Load the input image, resize and crop it to be the same size as the shirt image
input_image = Image.open(sys.argv[1])
input_image = ImageOps.fit(input_image, shirt.size)

# Paste the shirt image onto the input image and save it
input_image.paste(shirt, mask=shirt)
input_image.save(sys.argv[2])
