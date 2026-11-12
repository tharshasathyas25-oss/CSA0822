readings = [4, 6, 55, 1, 8, -60, 10, 3, 9]
valid = [c for c in readings if -50 <= c <= 50]
fahrenheit = [(c * 9/5) + 32 for c in valid]
alarm = [
    (i + 1, c)
    for i, c in enumerate(readings)
    if -50 <= c <= 50 and (c < 2 or c > 8)
]
print("Valid Readings:", valid)
print("Fahrenheit:", fahrenheit)
print("Alarm Minutes:", alarm)
