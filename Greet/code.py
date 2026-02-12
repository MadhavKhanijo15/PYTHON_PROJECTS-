import time
timestamp=time.strftime("%H:%M:%S")
print(timestamp)
time_stamp=int(time.strftime("%H"))
if 0<=int(time_stamp)<=12:
    print("Good Morning Sir")
if 12<int(time_stamp)<=16:
    print("Good Afternoon Sir")
if 16<int(time_stamp)<24:
    print("Goodevening Sir")
