
import time

def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text


def build_join(parts):
    return ";".join(parts) + ";"


def build_fstring(parts):
    lines = [f"{p};" for p in parts]
    return "".join(lines)


sizes = [1000, 10000, 200000]

for n in sizes:
    items = [f"Item{i}:Rs{i % 50}" for i in range(n)]

    start = time.perf_counter()
    result1 = build_plus(items)
    plus_time = time.perf_counter() - start

    start = time.perf_counter()
    result2 = build_join(items)
    join_time = time.perf_counter() - start

    start = time.perf_counter()
    result3 = build_fstring(items)
    fstring_time = time.perf_counter() - start

    print("\nNumber of lines:", n)
    print("Using += :", plus_time)
    print("Using join():", join_time)
    print("Using f-string:", fstring_time)

    print("All results same:", result1 == result2 == result3)
