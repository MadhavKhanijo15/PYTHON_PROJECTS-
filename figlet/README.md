Program based on FIGlet(a form of ASCII ART) , it can be implemented in python using pyfiglet module.

This program:
[As to run this program first install pyfiglet module using the following command - pip install pyfiglet]
Expects zero or two command-line arguments:
  Zero if the user would like to output text in a random font.
  Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program exits via sys.exit with an error message.
