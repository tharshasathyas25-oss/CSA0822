from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP = Decimal("0.40")
SNF_STEP = Decimal("0.20")


def calculate_rate(fat, snf):
    rate = (
        BASE_RATE
        + (fat - Decimal("3.5")) * FAT_STEP
        + (snf - Decimal("8.5")) * SNF_STEP
    )
    return rate


def calculate_payment(quantity, fat, snf):
    if quantity < 0:
        raise ValueError("Invalid quantity")

    if not Decimal("3.5") <= fat <= Decimal("7.0"):
        raise ValueError("Invalid fat value")

    if snf < Decimal("8.5"):
        raise ValueError("Invalid SNF value")

    payment = quantity * calculate_rate(fat, snf)

    return payment.quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )


payment = calculate_payment(
    Decimal("10"), Decimal("4.00"), Decimal("9.00")
)

print("Farmer Payment: Rs.", payment)
