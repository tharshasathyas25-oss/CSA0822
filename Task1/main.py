
MIN_FAT = 2.0
MAX_FAT = 7.0
DAYS = 10

farmers = {}

n = int(input("Enter number of farmers: "))

for i in range(n):
    print("\nFarmer", i + 1)

    farmer_id = input("Enter Farmer ID: ")
    litres = float(input("Enter milk quantity in litres: "))
    fat = float(input("Enter fat percentage: "))
    snf = float(input("Enter SNF percentage: "))
    shift = input("Enter shift (Morning/Evening): ").strip().lower()

    if litres < 0:
        print("Invalid quantity!")
        continue

    if not MIN_FAT <= fat <= MAX_FAT:
        print("Invalid fat percentage!")
        continue

    if snf < 0:
        print("Invalid SNF percentage!")
        continue

    if shift not in ("morning", "evening"):
        print("Invalid shift!")
        continue

    # Assumed formula for demonstration
    rate = (fat * 2) + (snf * 0.5)
    amount = litres * rate
    ten_day_total = amount * DAYS

    farmers[farmer_id] = {
        "litres": litres,
        "fat": fat,
        "snf": snf,
        "shift": shift,
        "rate": rate,
        "amount": amount,
        "ten_day_total": ten_day_total
    }

print("\n--- Milk Payment Details ---")

for farmer_id, details in farmers.items():
    print("\nFarmer ID:", farmer_id)
    print("Milk Quantity:", details["litres"], "litres")
    print("Fat Percentage:", details["fat"], "%")
    print("SNF Percentage:", details["snf"], "%")
    print("Shift:", details["shift"])
    print("Rate per Litre: Rs.", round(details["rate"], 2))
    print("Payment Amount: Rs.", round(details["amount"], 2))
    print("Ten-Day Total: Rs.",
          round(details["ten_day_total"], 2))
