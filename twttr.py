text = input("Input: ")
vowels = ["a" , "e" , "i" , "o" , "u" , "A" , "E" , "I" , "O" , "U"]

for c in text:
    for vowel in vowels:
        if c == vowel:
            text = text.replace(vowel, "", count=-1)
        else:
            pass

print(text)
