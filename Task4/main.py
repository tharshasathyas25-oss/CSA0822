
import math

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

fat = 4.2
snf = 8.7
litres = 8.5

fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)

rate = round(BASE_RATE + fat_steps * FAT_STEP_VALUE
             + snf_steps * SNF_STEP_VALUE, 2)
amount = round(litres * rate, 2)

print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate:", rate)
print("Amount:", amount)

print((4.2 - 3.5) / 0.1)
print(round((4.2 - 3.5) / 0.1))
print(-7 / 2, int(-7 / 2), math.floor(-7 / 2))
print(2.0 <= fat <= 7.0)
