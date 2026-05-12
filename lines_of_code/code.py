import sys

# Check if exactly one command-line argument is provided
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

# Check if file ends with .py
if not filename.endswith(".py"):
    sys.exit("Not a Python file")

try:
    count = 0

    with open(filename, "r") as file:
        for line in file:
            stripped = line.strip()

            # Ignore blank lines and comments
            if stripped == "" or stripped.startswith("#"):
                continue

            count += 1

    print(count)

except FileNotFoundError:
    sys.exit("File does not exist"
             
