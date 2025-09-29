def convert(text: str) -> str:
    text = text.replace(':)','🙂')
    text = text.replace(':(','🙁')
    return text


def main():
    text = input("Enter your text here.\n")
    print(convert(text))

main()