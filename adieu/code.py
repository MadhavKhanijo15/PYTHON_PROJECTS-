import inflect

p = inflect.engine()
names = []

try:
    while True:
        name = input("Name: ")
        if name:   # ignore empty lines
            names.append(name)
except EOFError:
    pass

print("\nAdieu, adieu, to " + p.join(names))
