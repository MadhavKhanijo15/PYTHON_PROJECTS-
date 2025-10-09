#Python program that prompts the user for mass as an integer(in kilograms) and then outputs the equivalent number of Joules as an integer. This program is based on Einstein's Energy-mass equivalence relation.

C=300000000
m=int(input("Whats the mass?"))
E=m*(C*C)

print("Equivalent value of joules-", E , "joules")
