"""Task 3: Runner-up score.

Read n, then n scores. Print the second-highest DISTINCT score.
"""

n = int(input())
scores = list(map(int, input().split()))

# A set removes duplicates, so repeated top scores count only once.
distinct = sorted(set(scores), reverse=True)
print(distinct[1])
