
import time

calls = 0

# Original recursive method
def ways_naive(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


# Redesigned loop method
def ways_loop(n):
    if n <= 1:
        return 1

    a = 1
    b = 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


sizes = [10, 20, 25, 30]

print("ORIGINAL VS REDESIGNED")

for n in sizes:

    calls = 0
    start = time.perf_counter()
    result1 = ways_naive(n)
    original_time = time.perf_counter() - start

    start = time.perf_counter()
    result2 = ways_loop(n)
    redesigned_time = time.perf_counter() - start

    print("\nSteps:", n)
    print("Original result:", result1)
    print("Original calls:", calls)
    print("Original time:", original_time)

    print("Redesigned result:", result2)
    print("Redesigned time:", redesigned_time)

    print("Results match:", result1 == result2)


# Test for 1000 steps
start = time.perf_counter()
large_result = ways_loop(1000)
loop_time = time.perf_counter() - start

print("\nFor 1000 steps:")
print("Number of digits:", len(str(large_result)))
print("Loop time:", loop_time)
