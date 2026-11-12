rainfall = [
    10, 20, 0, 15, 25, 5, 10,
    0, 5, 10, 20, 15, 0, 10,
    30, 25, 20, 10, 5, 0, 15
]
weekly_totals = []
for i in range(0, len(rainfall), 7):
    week = rainfall[i:i+7]
    weekly_totals.append(sum(week))
wettest = max(weekly_totals)
driest = min(weekly_totals)
moving_average = []
for i in range(len(rainfall) - 6):
    avg = sum(rainfall[i:i+7]) / 7
    moving_average.append(round(avg, 2))
dry_days = []
for i in range(len(rainfall)):
    if rainfall[i] == 0:
        dry_days.append(i + 1)
print("Weekly Rainfall Totals:", weekly_totals)
print("Wettest Week Rainfall:", wettest)
print("Driest Week Rainfall:", driest)
print("7-Day Moving Average:", moving_average)
print("Dry Days:", dry_days)
