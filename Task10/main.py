from decimal import Decimal, ROUND_HALF_UP
import time

sizes = [300, 6000, 150000]

for n in sizes:
    float_payments = [0.1] * n
    decimal_payments = [Decimal("0.10")] * n

    start = time.perf_counter()
    float_total = sum(float_payments)
    float_time = time.perf_counter() - start

    start = time.perf_counter()
    decimal_total = sum(decimal_payments)
    decimal_time = time.perf_counter() - start

    print("\nEntries:", n)
    print("Float total:", float_total)
    print("Decimal total:", decimal_total)
    print("Difference:", abs(
        Decimal(str(float_total)) - decimal_total
    ))
    print("Float time:", float_time)
    print("Decimal time:", decimal_time)

    rounded_total = decimal_total.quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )
    print("Rounded bank total:", rounded_total)
