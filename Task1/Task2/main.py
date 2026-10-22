
MIN_FAT = 2.0
MAX_FAT = 7.0
DAYS = 10

farmers = {}
n = int(input("Enter number of farmers: "))

for i in range(n):
    farmer_id = input("Enter Farmer ID: ")
    litres = float(input("Enter litres: "))
    fat = float(input("Enter fat %: "))
    snf = float(input("Enter SNF %: "))
    shift = input("Enter shift: ")

    if litres < 0 or not MIN_FAT <= fat <= MAX_FAT or snf < 0:
        print("Invalid input")
        continue

    rate = (fat * 2) + (snf * 0.5)
    amount = litres * rate

    farmers[farmer_id] = {
        "rate": rate,
        "amount": amount,
        "total": amount * DAYS
    }

for fid, data in farmers.items():
    print("Farmer ID:", fid)
    print("Rate per litre:", data["rate"])
    print("Payment:", data["amount"])
    print("Ten-day total:", data["total"])
