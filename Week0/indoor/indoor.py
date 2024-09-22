def main():
    # get user yelling (text in uppercase)
    yelling = input()

    # say in lower voice (text in lowercase)
    print(indoor_voice(yelling))


def indoor_voice(text):
    return text.lower()


main()