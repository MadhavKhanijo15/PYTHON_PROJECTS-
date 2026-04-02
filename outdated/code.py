months=[ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]
while True:
    try:
        date=input("Date: ").strip()
        #case 1: MM/DD/YYYY
        if "/" in date:
            month,day,year=date.split("/")
        #case 2: Month DD , YYYY
        elif  "," in date:
            parts=date.split()
            month=str(months.index(parts[0])+1)
            day=parts[1].replace(",","")
            year=parts[2]
        else:
            continue

        #convert to int
        month=int(month)
        day=int(day)
        year=int(year)

        if 1<=month<=12 and 1<=day<=31:
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

    except(ValueError , IndexError):
        pass
