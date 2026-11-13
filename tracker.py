"""Placement Readiness Tracker - IRP-II (CSE2596) Assignment.

Records practice-test scores for students, calculates results
and flags students who need extra practice.
"""

# Task 1: students stored as a list of dictionaries.
# Each score is out of 100.
students = [
    {"name": "Aarav Sharma", "roll_no": "2301001", "aptitude": 82, "verbal": 75, "coding": 90},
    {"name": "Diya Mehta",   "roll_no": "2301002", "aptitude": 65, "verbal": 70, "coding": 58},
    {"name": "Rohan Verma",  "roll_no": "2301003", "aptitude": 35, "verbal": 42, "coding": 30},
    {"name": "Sneha Iyer",   "roll_no": "2301004", "aptitude": 91, "verbal": 88, "coding": 95},
    {"name": "Kabir Singh",  "roll_no": "2301005", "aptitude": 48, "verbal": 55, "coding": 40},
]


def read_score(subject):
    """Keep asking until the user enters an integer between 0 and 100."""
    while True:
        text = input(f"Enter {subject} score (0-100): ")
        try:
            value = int(text)          # input() returns str, so convert
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if 0 <= value <= 100:
            return value
        print("  Score must be between 0 and 100. Try again.")


def add_student(students):
    """Read one new student from the keyboard and append to the list."""
    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()
    student = {
        "name": name,
        "roll_no": roll_no,
        "aptitude": read_score("aptitude"),
        "verbal": read_score("verbal"),
        "coding": read_score("coding"),
    }
    students.append(student)
    print(f"Added {name}.\n")


if __name__ == "__main__":
    add_student(students)
    print("Total students:", len(students))
