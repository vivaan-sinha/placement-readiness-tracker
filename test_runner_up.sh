#!/bin/bash
# Runs runner_up.py against test cases: input | expected output
check() {
  actual=$(printf "%s" "$1" | python3 runner_up.py)
  [ "$actual" == "$2" ] && r=PASS || r=FAIL
  echo "$r  expected=$2 actual=$actual"
}
check $'5\n70 85 85 60 90\n' 85
check $'4\n90 90 90 70\n' 70
check $'2\n0 100\n' 0
check $'6\n55 55 80 80 80 60\n' 60
