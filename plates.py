def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    x = len(s)
    if 2 <= x <= 6:
        if s.isalpha():
            return True

    if 2 <= x <= 6:
        if s[0:2].isalpha():
            if s.isalnum():
                if not s[x-1].isalpha():
                    if s[x-2:x].isdigit():
                        if s[x-2] != "0":
                            return True

main()
