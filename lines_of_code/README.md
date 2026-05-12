One way to measure the complexity of a program is to count its number of lines of code (LOC), excluding blank lines and comments.
This program expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in '.py', or if the specified file does not exist, the program instead exits via sys.exit.

Assuming that any line that starts with #, optionally preceded by whitespace, is a comment.
