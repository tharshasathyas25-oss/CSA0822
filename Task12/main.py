from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("32.00")
FAT_STEP = Decimal("0.45")
SNF_STEP = Decimal("0.20")
BONUS_RATE = Decimal("0.50")

MIN_FAT = Decimal("3.50")
MAX_FAT = Decimal("7.00")
MIN_SNF = Decimal("8.50")


def calculate_rate(fat, snf):
    return (
        BASE_RATE
        + (fat - MIN_FAT) * FAT_STEP
        + (snf - MIN_SNF) * SNF_STEP
    )


def calculate_payment(quantity, fat, snf):
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError("Fat value is outside the allowed range")

    if snf < MIN_SNF:
        raise ValueError("SNF value is below the minimum")

    rate = calculate_rate(fat, snf)

    return (quantity * rate).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )


def final_payment(entries):
    total_quantity = sum(q for q, f, s in entries)
    total_payment = sum(
        (calculate_payment(q, f, s) for q, f, s in entries),
        Decimal("0.00")
    )

    if total_quantity > Decimal("500"):
        bonus = total_quantity * BONUS_RATE
        total_payment += bonus

    return total_payment.quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )


entries = [
    (Decimal("200"), Decimal("4.00"), Decimal("9.00")),
    (Decimal("180"), Decimal("4.50"), Decimal("9.20")),
    (Decimal("150"), Decimal("5.00"), Decimal("9.50"))
]

print("Total Quantity:", sum(q for q, f, s in entries), "litres")
print("Final Payment: Rs.", final_payment(entries))
