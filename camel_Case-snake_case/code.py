camel=str(input("CamelCase: "))
snake=" "
for ch in camel:
    if ch.isupper():
        snake += "_" + ch.lower()
    else:
        snake += ch
print(snake)
