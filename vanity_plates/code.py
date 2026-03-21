def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1 & 2: Length must be between 2 and 6, and start with 2 letters
    if not (2 <= len(s) <= 6) or not s[0:2].isalpha():
        return False
    #Rule 3: Only letters and numbers
    if not s.isalnum():
        return False
    # Rule 4: Numbers at the end, and the first number cannot be '0'
    number_started = False
    for char in s:
        if char.isdigit():
            # If this is the very first digit encountered
            if not number_started:
                if char == '0':
                    return False  # First number cannot be '0'
                number_started = True

        # If we encounter a letter AFTER a number has already appeared
        elif number_started:
            return False

    return True

main()
