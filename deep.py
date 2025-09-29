answer = input("What is the answer to the Great Question of life, the universe, and everything?\n")
answer = answer.casefold()
answer = answer.replace(' ','')

if answer == str(42):
    print("Yes")
elif answer == "forty-two":
    print("Yes")
elif answer == "fortytwo":
    print("Yes")
else:
    print("No")
