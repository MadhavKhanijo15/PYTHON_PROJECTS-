import sys
import csv

# Check command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

before = sys.argv[1]
after = sys.argv[2]

students = []

try:
    # Read before.csv
    with open(before, "r") as infile:
        reader = csv.DictReader(infile)

        for row in reader:
            last, first = row["name"].split(", ")

            students.append({
                "first": first,
                "last": last,
                "house": row["house"]
            })

    # Write after.csv
    with open(after, "w", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])

        writer.writeheader()

        for student in students:
            writer.writerow(student)

except FileNotFoundError:
    sys.exit(f"Could not read {before}")
