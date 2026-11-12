
correct_otp = "1234"
attempts = 0

while attempts < 3:
    otp = input("Enter OTP: ")

    if otp == "":
        pass
        continue

    attempts += 1

    if otp == correct_otp:
        print("OTP Verified Successfully")
        break
    else:
        print("Incorrect OTP")

else:
    print("Account locked for 30 minutes")
