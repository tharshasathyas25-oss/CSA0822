
def calculate_payment(litres, fat, snf):
    if litres < 0 or not 2.0 <= fat <= 7.0 or snf < 0:
        return None

    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = round(30 + fat_steps * 0.4
                 + snf_steps * 0.3, 2)
    amount = round(litres * rate, 2)
    total = round(amount * 10, 2)

    return rate, amount, total

entries = [
    (10, 3.5, 8.5),
    (8.5, 4.2, 8.7),
    (12, 3.1, 8.3)
]

for litres, fat, snf in entries:
    result = calculate_payment(litres, fat, snf)
    if result is None:
        print("Invalid input")
    else:
        print("Rate, payment, ten-day total:", result)
