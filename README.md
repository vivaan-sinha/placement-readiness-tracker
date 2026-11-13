# Placement Readiness Tracker

A small command-line tool for a college placement cell. It records students'
practice-test scores (aptitude, verbal, coding), calculates each student's
average and grade, finds the top scorer and flags students who need extra practice.

Built for **IRP-II (CSE2596) Assignment**, B.Tech CSE Semester V, IILM University.

## Files

| File | Purpose |
|------|---------|
| `tracker.py` | Main program (Tasks 1 and 2) |
| `runner_up.py` | Second-highest distinct score, reads from stdin (Task 3) |
| `test_runner_up.sh` | Runs `runner_up.py` on several test cases |

## How to run

Requires Python 3.8+.

```bash
python tracker.py          # asks for one new student, then prints results
python runner_up.py        # enter n, then n scores
./test_runner_up.sh        # run the test cases
```

## Grading rules

| Average | Grade |
|---------|-------|
| 80 and above | A |
| 60 and above | B |
| 40 and above | C |
| below 40 | Needs practice |

## Sample output

```
Enter student name: Meera Nair
Enter roll number: 2301006
Enter aptitude score (0-100): 150
  Score must be between 0 and 100. Try again.
Enter aptitude score (0-100): abc
  Please enter a whole number.
Enter aptitude score (0-100): -5
  Score must be between 0 and 100. Try again.
Enter aptitude score (0-100): 72
Enter verbal score (0-100): 68
Enter coding score (0-100): 40
Added Meera Nair.

--------------------------------------------------------------------------
Roll No   Name              Apt  Verb  Code     Avg   Grade
--------------------------------------------------------------------------
2301001   Aarav Sharma       82    75    90   82.33   A
2301002   Diya Mehta         65    70    58   64.33   B
2301003   Rohan Verma        35    42    30   35.67   Needs practice
2301004   Sneha Iyer         91    88    95   91.33   A
2301005   Kabir Singh        48    55    40   47.67   C
2301006   Meera Nair         72    68    40   60.00   B
--------------------------------------------------------------------------

Top scorer: Sneha Iyer (91.33)
Needs extra practice:
  - Rohan Verma (2301003) avg 35.67
```

## Git workflow

Developed in small commits. The grade/result functions were built on the
`feature-grades` branch and merged into `main`.
