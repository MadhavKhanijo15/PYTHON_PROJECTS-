#A program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

answer=input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
if answer.strip().lower()=="42" or answer.strip().lower()=="forty-two" or answer.strip().lower()=="forty two":
    print("Yes")

else :
    print("No")
