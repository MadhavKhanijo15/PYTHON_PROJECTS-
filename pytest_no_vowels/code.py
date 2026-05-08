def main():
    word=str(input("Input: "))
    print("Output: " ,shorten(word))


def shorten(word):
    vowels="aeiouAEIOU"
    output= ""

    for ch in word:
        if ch not in vowels:
            output += ch
    return output

if __name__ == "__main__":
    main()
