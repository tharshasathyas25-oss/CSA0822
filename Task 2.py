import os
attendance = []
errors = []
folder = "."
for filename in os.listdir(folder):
    if filename.startswith("attendance") and filename.endswith(".txt"):
        path = os.path.join(folder, filename)
        try:
            with open(path, "r", encoding="utf-8") as f:
                for line_no, line in enumerate(f, 1):
                    try:
                        parts = line.strip().split(",")
                        if len(parts) != 3:
                            raise ValueError("Invalid record format")
                        reg_no, date, status = parts
                        if status.strip() not in ["Present", "Absent", "P", "A"]:
                            raise ValueError("Invalid status")
                        attendance.append((reg_no.strip(), date.strip(), status.strip()))
                    except ValueError as e:
                        errors.append(f"{filename} - Line {line_no}: {e}")
        except OSError as e:
            errors.append(f"{filename}: {e}")
print("Attendance Records:")
for record in attendance:
    print(record)
print("\nErrors:")
if errors:
    for error in errors:
        print(error)
else:
    print("No errors found")
