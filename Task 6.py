trains = {
    "101": {
        "name": "Chennai Express",
        "stations": [
            ("Salem", "08:00", "08:10"),
            ("Erode", "09:00", "09:05")
        ],
        "days": {"Monday", "Tuesday", "Wednesday"}
    },
    "102": {
        "name": "Bangalore Express",
        "stations": [
            ("Salem", "07:00", "07:15"),
            ("Erode", "08:00", "08:10")
        ],
        "days": {"Monday", "Friday"}
    },
    "103": {
        "name": "Coimbatore Express",
        "stations": [
            ("Salem", "10:00", "10:10"),
            ("Erode", "11:00", "11:05")
        ],
        "days": {"Tuesday", "Thursday"}
    },
    "104": {
        "name": "Mysore Express",
        "stations": [
            ("Salem", "06:00", "06:10"),
            ("Erode", "07:00", "07:10")
        ],
        "days": {"Monday", "Wednesday"}
    },
    "105": {
        "name": "Kerala Express",
        "stations": [("Salem", "12:00", "12:10"),
            ("Erode", "13:00", "13:10")],
        "days": {"Friday", "Saturday"}
    }
}
station = "Salem"
day = "Monday"
result = []
for number, details in trains.items():
    if day in details["days"]:
        for stop in details["stations"]:
            if stop[0] == station:
                result.append((number, details["name"], stop[2]))
result = sorted(result, key=lambda x: x[2])
print("Trains stopping at", station, "on", day)
for train in result:
    print("Train No:", train[0])
    print("Train Name:", train[1])
    print("Departure:", train[2])
    print()
