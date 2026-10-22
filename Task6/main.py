
BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def rate_per_litre(fat, snf):
    """Calculate milk rate per litre."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(BASE_RATE + fat_steps * FAT_STEP_VALUE
                 + snf_steps * SNF_STEP_VALUE, 2)

def payout(litres, fat, snf):
    """Calculate payment for the milk supplied."""
    return round(litres * rate_per_litre(fat, snf), 2)

def ten_day_total(daily_amount):
    """Calculate payment for ten days."""
    return round(daily_amount * 10, 2)

rate = rate_per_litre(4.2, 8.7)
amount = payout(8.5, 4.2, 8.7)
total = ten_day_total(amount)

print("Rate:", rate)
print("Payout:", amount)
print("Ten-day total:", total)
