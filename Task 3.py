import os
import tempfile
class InvalidRecord(Exception):
    """Custom exception for invalid attendance records."""
def parse_line(line):
    parts = line.strip().split(",")
    if len(parts) != 3:
        raise InvalidRecord(
            f"expected 3 fields, found {len(parts)}"
        )
    status = parts[2]
    if status not in ("P", "A"):
        try:
            raise ValueError(f"invalid status '{status}'")
        except ValueError as e:
            raise InvalidRecord(str(e)) from e
    return tuple(parts)
def summarise(path):
    present, absent, errors = 0, 0, []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_no, line in enumerate(file, start=1):
                try:
                    record = parse_line(line)
                except InvalidRecord as e:
                    errors.append((line_no, str(e)))
                else:
                    if record[2] == "P":
                        present += 1
                    else:
                        absent += 1
    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError:
        print("Error: Permission denied")
    finally:
        print("File processing completed")
    return present, absent, errors
data = ("192311001,2026-10-08,P\n"
        "192311002,2026-10-08,A\n"
        "192311003,2026-10-08\n"
        "192311004,2026-10-08,L\n")
with tempfile.NamedTemporaryFile(
    "w", suffix=".csv", delete=False, encoding="utf-8"
) as tmp:
    tmp.write(data)
print(summarise(tmp.name))
os.remove(tmp.name)
