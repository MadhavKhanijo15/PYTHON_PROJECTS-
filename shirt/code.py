import sys
import os
from PIL import Image, ImageOps

# Check command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

# Valid extensions
valid_extensions = [".jpg", ".jpeg", ".png"]

input_ext = os.path.splitext(input_file)[1].lower()
output_ext = os.path.splitext(output_file)[1].lower()

# Check file extensions
if input_ext not in valid_extensions or output_ext not in valid_extensions:
    sys.exit("Invalid output")

# Check matching extensions
if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

try:
    # Open input image
    photo = Image.open(input_file)

except FileNotFoundError:
    sys.exit("Input does not exist")

# Open shirt image
shirt = Image.open("shirt.png")

# Resize and crop input image to match shirt size
size = shirt.size
photo = ImageOps.fit(photo, size)

# Overlay shirt on top of photo
photo.paste(shirt, shirt)

# Save result
photo.save(output_file)
