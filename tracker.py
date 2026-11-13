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

if __name__ == "__main__":
    print("Loaded", len(students), "students")
