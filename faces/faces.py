#Making faces-Implement a python program that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text is returned unchanged.

def main():
    ask=input("Happy face or Sad face?")
    result=convert(ask)
    print(result)

def convert(message):
    message=message.replace(":)" , "🙂")
    message=message.replace(":(" , "🙁")
    return message

main()
