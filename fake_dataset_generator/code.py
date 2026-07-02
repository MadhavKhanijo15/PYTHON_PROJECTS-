import random
import csv


def main():
    choice = input(
        "Choose Database:\n"
        "1. Student Database\n"
        "2. Office-Employees Database\n\n"
        "Enter choice: "
    )

    rows = int(input("Enter number of subject IDs/records: "))

    return choice, rows


def generate_student(rows):
    names = [
        "Thomas", "Anne", "Rahul", "Daniel", "Harry", "Emily",
        "Charles", "George", "Henry", "Alice", "Lily", "Freddie",
        "Bonnie", "Matilda", "Victoria", "Sophia", "John", "Robert",
        "Taylor", "Travis", "James", "Amelia", "Michael", "William",
        "Olivia", "Pawan", "Noah", "Jennifer", "Jessica",
        "Lawrence", "Scottie", "Nyra"
    ]

    records = []

    for i in range(rows):
        records.append({
            "student_id": [i+1],
            "name": random.choice(names),
            "age": random.randint(18, 25),
            "weight": round(random.uniform(45.0, 100.0), 1),
            "height": round(random.uniform(150.0, 200.0), 1),
            "BMI": round(random.uniform(18.5, 25.0), 1)
        })

    return records


def generate_office(rows):
    names = [
        "Thomas", "Anne", "Rahul", "Daniel", "Harry", "Emily",
        "Charles", "George", "Henry", "Alice", "Lily", "Freddie",
        "Bonnie", "Matilda", "Victoria", "Sophia", "John", "Robert",
        "Taylor", "Travis", "James", "Amelia", "Michael", "William",
        "Olivia", "Pawan", "Noah", "Jennifer", "Jessica",
        "Lawrence", "Scottie", "Nyra"
    ]

    departments = [
        "HR", "Finance", "Marketing",
        "Sales", "IT", "Legal", "Support"
    ]

    records = []

    for i in range(rows):
        records.append({
            "employee_id": [i+1],
            "name": random.choice(names),
            "age": random.randint(23, 60),
            "department": random.choice(departments),
            "salary": random.randint(50000, 1000000),
            "joining_year": random.randint(2010, 2026)
        })

    return records


def save_csv(records, filename):
    if not records:
        return

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=records[0].keys()
        )

        writer.writeheader()
        writer.writerows(records)

    print(f"\nDataset saved as {filename}")


# Main Program
if __name__ == "__main__":
    choice, rows = main()

    if choice == "1":
        records = generate_student(rows)
        save_csv(records, "students.csv")

    elif choice == "2":
        records = generate_office(rows)
        save_csv(records, "office.csv")
