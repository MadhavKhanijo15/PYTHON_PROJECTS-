import sys
import csv
from tabulate import tabulate

# Check for exactly one command-line argument
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

# Check if file is CSV
if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    table = []

    with open(filename, "r") as file:
        reader = csv.reader(file)

        # Read all rows into table
        for row in reader:
            table.append(row)

    # Print table in grid format
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
