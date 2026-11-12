
from functools import lru_cache
import sys

calls = 0

# Normal recursive function
def ways_naive(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


# Recursive function using memoisation
@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


# Loop method
def ways_loop(n):
    if n <= 1:
        return 1

    a = 1
    b = 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


# Compare function calls
for n in [10, 20, 25, 30]:

    calls = 0
    result1 = ways_naive(n)
    print("Naive:", n, result1, "Calls:", calls)

    calls = 0
    ways_memo.cache_clear()
    result2 = ways_memo(n)
    print("Memo :", n, result2, "Calls:", calls)


# Test for 1000 steps
print("Recursion limit:", sys.getrecursionlimit())

try:
    print("Memoised result for 1000:", ways_memo(1000))
except RecursionError:
    print("RecursionError occurred")

print("Loop result for 1000:", ways_loop(1000))
