
BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
BASE_FAT = 3.5
BASE_SNF = 8.5

fat = 4.2
snf = 8.7

fat_steps = round((fat - BASE_FAT) / 0.1)
snf_steps = round((snf - BASE_SNF) / 0.1)

rate = round(BASE_RATE + fat_steps * FAT_STEP_VALUE
             + snf_steps * SNF_STEP_VALUE, 2)

print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate per litre:", rate)

value = 10
print(type(value))
value = "Hello"
print(type(value))

a, b = 10, 20
a, b = b, a
print("After swapping:", a, b)
