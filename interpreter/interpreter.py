'''Program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assuming that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein: '''

Prompt=str(input("Expression:"))
x, op, z = Prompt.split()
X=int(x)
Z=int(z)
if op=="+":
    result=X + Z
elif op=="-":
    result=X - Z
elif op=="*":
    result=X * Z
elif op=="/":
    result=X / Z
else: print("Invalid Operator")

print(f"{result:.1f}")
