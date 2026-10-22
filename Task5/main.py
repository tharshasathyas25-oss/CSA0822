
BASE_RATE = 30.00

farmer_id = input("Enter Farmer ID: ")

try:
    litres = float(input("Enter litres: "))
    fat = float(input("Enter fat %: "))
    snf = float(input("Enter SNF %: "))

    if litres < 0 or not 2.0 <= fat <= 7.0 or snf < 0:
        print("Invalid values")
    else:
        fat_steps = round((fat - 3.5) / 0.1)
        snf_steps = round((snf - 8.5) / 0.1)
        rate = round(30 + fat_steps * 0.4
                     + snf_steps * 0.3, 2)
        amount = round(litres * rate, 2)

        print(f"Farmer: {farmer_id}")
        print(f"Rate: Rs. {rate:.2f}")
        print(f"Amount: Rs. {amount:.2f}")

except ValueError:
    print("Please enter valid numbers.")
