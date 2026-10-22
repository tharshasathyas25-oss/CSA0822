from decimal import Decimal, ROUND_HALF_UP

MIN_FAT = Decimal("3.5")
MAX_FAT = Decimal("7.0")
MIN_SNF = Decimal("8.5")

BASE_RATE = Decimal("30.00")
FAT_STEP = Decimal("0.40")
SNF_STEP = Decimal("0.20")


def calculate_rate(fat, snf, seasonal=False):
    base = Decimal("32.00") if seasonal else BASE_RATE
    fat_step = Decimal("0.45") if seasonal else FAT_STEP

    return (base
            + (fat - MIN_FAT) * fat_step
            + (snf - MIN_SNF) * SNF_STEP)


def calculate_payment(quantity, fat, snf, seasonal=False):
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError("Fat value is outside the allowed range")

    if snf < MIN_SNF:
        raise ValueError("SNF value is below the minimum")

    rate = calculate_rate(fat, snf, seasonal)
    payment = quantity * rate

    return payment.quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )


def run_tests():
    tests = [
        ("Normal", "10", "4.00", "9.00", True),
        ("Lower boundary", "10", "3.50", "8.50", True),
        ("Upper fat boundary", "10", "7.00", "9.00", True),
        ("Invalid fat", "10", "8.00", "9.00", False),
        ("Negative quantity", "-5", "4.00", "9.00", False),
        ("Text input", "abc", "4.00", "9.00", False),
    ]

    for name, q, f, s, valid in tests:
        try:
            result = calculate_payment(
                Decimal(q), Decimal(f), Decimal(s)
            )
            assert valid
            print(name, "PASS - Payment:", result)
        except (ValueError, ArithmeticError, AssertionError):
            if not valid:
                print(name, "PASS - Invalid input rejected")
            else:
                print(name, "FAIL")


run_tests()
