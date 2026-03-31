while True:
    try:
        frac=input("Enter fraction (x/y): ")
        x,y = frac.split("/")
        x=int(x)
        y=int(y)
        
        if x < 0 or y <= 0:
            raise ValueError
        if y==0:
            raise ZeroDivisionError

        if x>y:
            raise ValueError

    except (ValueError, ZeroDivisionError):
        continue
    else:
        break
z= round((x/y)*100)

if z<=1 :
    print("Your fuel percentage is: E")
elif z>=99:
    print("Your fuel percentage is: F")
else:
    print(f"{z}%")
