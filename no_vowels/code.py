text=str(input("Input: "))
vowels="aeiouAEIOU"
output= ""

for ch in text:
    if ch not in vowels:
        output += ch

print("Output: " , output)
