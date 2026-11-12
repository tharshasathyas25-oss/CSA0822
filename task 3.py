
def normalise(text):
    return text.strip().replace(" ", "").replace("-", "").upper()


def is_valid(reg):
    if len(reg) not in (9, 10):
        return False

    state = reg[:2]
    district = reg[2:4]
    series = reg[4:-4]
    number = reg[-4:]

    return (state.isalpha() and
            district.isdigit() and
            series.isalpha() and
            number.isdigit())


def format_number(reg):
    return reg[:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]


vehicles = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "Tn09Ab1234",
    "TN9AB1234",
    "TN 22 1234 AB",
    "KL 07 CD 5678"
]

for raw in vehicles:
    reg = normalise(raw)

    if is_valid(reg):
        print(raw, "->", reg, "VALID")
        print("Receipt:", format_number(reg))
    else:
        print(raw, "->", reg, "INVALID")
