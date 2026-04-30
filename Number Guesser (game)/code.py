import random

#Taking input of level
while True:
    try:
        in_n=int(input("Level: "))
        if in_n<1:
            continue
        break
    except ValueError:
        continue

#Randomly setting value of number
number=random.randint(1,in_n)

#Asking for guess
while True:
    try:
        Guess=int(input("Guess:"))
        if Guess<1:
            Guess=int(input("Guess:"))
        break
    except ValueError:
        continue
#Core Logic
if Guess<number:
    print("Too small!")
    Guess=int(input("Guess:"))
if Guess>number:
    print("Too large!")
    Guess=int(input("Guess:"))
if Guess==number:
    print("Just right!")
