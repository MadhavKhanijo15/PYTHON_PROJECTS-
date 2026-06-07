import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"

    match = re.match(pattern, s)
    if not match:
        raise ValueError

    h1, m1, p1, h2, m2, p2 = match.groups()

    # Default minutes if not provided
    m1 = m1 if m1 else "00"
    m2 = m2 if m2 else "00"

    h1, h2 = int(h1), int(h2)
    m1_int, m2_int = int(m1), int(m2)

    # Validate hours and minutes
    if not (1 <= h1 <= 12 and 1 <= h2 <= 12):
        raise ValueError

    if not (0 <= m1_int <= 59 and 0 <= m2_int <= 59):
        raise ValueError

    # Convert first time
    if p1 == "AM":
        if h1 == 12:
            h1 = 0
    else:  # PM
        if h1 != 12:
            h1 += 12

    # Convert second time
    if p2 == "AM":
        if h2 == 12:
            h2 = 0
    else:  # PM
        if h2 != 12:
            h2 += 12

    return f"{h1:02}:{m1} to {h2:02}:{m2}"


if __name__ == "__main__":
    main()
