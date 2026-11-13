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


# Task 2: functions
def average(student):
    """Return the mean of the three scores."""
    total = student["aptitude"] + student["verbal"] + student["coding"]
    return total / 3


def grade(avg):
    """Return a grade for an average: A, B, C or 'Needs practice'."""
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Needs practice"


def top_scorer(students):
    """Return the student with the highest average."""
    best = students[0]
    for s in students:
        if average(s) > average(best):
            best = s
    return best


def needs_practice(students, limit=40):
    """Return the students whose average is below limit (default 40)."""
    weak = []
    for s in students:
        if average(s) < limit:
            weak.append(s)
    return weak


def print_table(students):
    """Print a neatly formatted result table."""
    line = "-" * 74
    print(line)
    print(f"{'Roll No':<10}{'Name':<16}{'Apt':>5}{'Verb':>6}{'Code':>6}{'Avg':>8}   Grade")
    print(line)
    for s in students:
        avg = average(s)
        print(f"{s['roll_no']:<10}{s['name']:<16}{s['aptitude']:>5}{s['verbal']:>6}"
              f"{s['coding']:>6}{avg:>8.2f}   {grade(avg)}")
    print(line)


if __name__ == "__main__":
    add_student(students)
    print_table(students)
    best = top_scorer(students)
    print(f"\nTop scorer: {best['name']} ({average(best):.2f})")
    print("Needs extra practice:")
    weak = needs_practice(students)
    if weak:
        for s in weak:
            print(f"  - {s['name']} ({s['roll_no']}) avg {average(s):.2f}")
    else:
        print("  None")
