import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    fonts = figlet.getFonts()
    font = random.choice(fonts)

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in figlet.getFonts():
            font = sys.argv[2]
        else:
            sys.exit("Invalid font")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

#Taking Input
input_ = input("Input: ")

# Output
print("Output:")
figlet.setFont(font=font)
print(figlet.renderText(input_))
