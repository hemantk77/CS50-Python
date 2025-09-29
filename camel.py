text = input("camelCase: ")
result = ""

for c in text:
    if c.isupper() == True:
        result += "_" + c
    else:
        result += c

result = result.lower()

print(result)