coke = 50
print(f"Amount Due: {coke}")

while coke > 0:
    money = int(input("Insert Coin: "))
    if money == 25:
        coke -= money
        print(f"Amount Due: {coke}")
    elif money == 10:
        coke -= money
        print(f"Amount Due: {coke}")
    elif money == 5:
        coke -= money
        print(f"Amount Due: {coke}")
    else:
       print(f"Amount Due: {coke}")

if coke == 0:
    print("Change Owed: 0")
else:
    coke = abs(coke)
    print(f"Change Owed: {coke}")
