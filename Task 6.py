import os
seen = set()
students = []
errors = []
events = {}
files = ["CSE.txt", "ECE.txt", "EEE.txt",
         "MECH.txt", "CIVIL.txt"]
for filename in files:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                try:
                    parts = line.strip().split(",")
                    if len(parts) != 5:
                        raise ValueError("Damaged line")
                    reg, name, dept, email, event = parts
                    if "@" not in email or "." not in email.split("@")[-1]:
                        raise ValueError("Invalid email")
                    if reg in seen:
                        raise ValueError("Duplicate registration")
                    seen.add(reg)
                    students.append(line.strip())
                    for e in event.split(";"):
                        e = e.strip()
                        events.setdefault(e, []).append(reg + "," + name)
                except ValueError as e:
                    errors.append(f"{filename}, Line {line_no}: {e}")
    except FileNotFoundError:
        errors.append(f"{filename}: File not found")
with open("master_list.txt", "w", encoding="utf-8") as f:
    for student in students:
        f.write(student + "\n")
for event, participants in events.items():
    with open(event + ".txt", "w", encoding="utf-8") as f:
        for student in participants:
            f.write(student + "\n")
with open("summary.txt", "w", encoding="utf-8") as f:
    f.write("Total Registrations: " + str(len(students)) + "\n")
    f.write("Total Events: " + str(len(events)))
with open("error_log.txt", "w", encoding="utf-8") as f:
    for error in errors:
        f.write(error + "\n")
print("Registration processing completed")
print("Total Students:", len(students))
print("Errors:", len(errors))