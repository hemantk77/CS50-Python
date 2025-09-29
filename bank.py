reply = input("How would you like to greet the customer?\n")

reply = reply.casefold()
reply = reply.replace(' ','')

if reply.startswith("hello") == True:
    print("$0")
elif reply.startswith("h") == True:
    print("$20")
else:
    print("$100")
