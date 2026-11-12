units = int(input("Enter electricity units: "))
ration = input("Do you have a ration card (yes/no): ").lower()
age = int(input("Enter age of oldest family member: "))

print("\nUsing Separate If Statements:")

if units <= 100:
    print("Full Subsidy Eligible")

if units <= 200 and ration == "yes":
    print("Partial Subsidy Eligible")

if units > 200 and age > 80:
    print("Special Subsidy Eligible")

print("\nUsing If-Elif-Else:")

if units <= 100:
    print("Full Subsidy Eligible")
elif 101 <= units <= 200:
    if ration == "yes":
        print("Partial Subsidy Eligible")
    else:
        print("No Subsidy")
elif units > 200:
    if age > 80:
        print("Special Subsidy Eligible")
    else:
        print("No Subsidy")