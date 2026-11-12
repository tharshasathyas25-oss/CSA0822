from decimal import Decimal, InvalidOperation
def process_mess_file(filename):
    total = Decimal("0.00")
    report = []
    rejected = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line_number, line in enumerate(f, start=1):
                if not line.strip():
                    continue
                try:
                    parts = line.strip().split(",")
                    if len(parts) != 3:
                        raise ValueError("Expected 3 fields")
                    reg_no, name, amount = parts
                    amount = Decimal(amount)
                    total += amount
                    report.append(f"{name} {amount:.2f}")
                except (ValueError, InvalidOperation) as e:
                    rejected.append((line_number, str(e)))
        print("Mess Bill Report")
        print("\n".join(report))
        print("Total:", f"{total:.2f}")
        print("Rejected Records:", rejected)
    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError:
        print("Error: Permission denied")
    except UnicodeDecodeError:
        print("Error: Unable to read file encoding")
process_mess_file("mess_oct.txt")
