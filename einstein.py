def einstein(text : int) -> int:
    c = 300000000
    text = text * c
    text = text * c
    return text

text = int(input("m: "))

print("E:", einstein(text))
