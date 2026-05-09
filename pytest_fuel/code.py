def main():
    while True:
        try:
            fraction = input("Fraction(x/y): ")
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            print(gauge(percentage))
            break

def convert(fraction):
    x,y = fraction.split("/")
    x=int(x)
    y=int(y)

    if y==0:
        raise ZeroDivisionError

    if x>y:
        raise ValueError

    percentage=int(round((x/y)*100))
    return percentage


def gauge(percentage):
    if percentage<=1 :
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
