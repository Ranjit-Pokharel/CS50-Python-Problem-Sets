import emoji


def main():
    # get codes from user
    codes = get_codes("Input: ")

    # convert the codes to emoji
    convert_to_emoji(codes)


def get_codes(promp):
    codes = input(promp).strip()
    return codes


def convert_to_emoji(codes):
    print("Output:", emoji.emojize(codes, language="alias"))


if __name__ == "__main__":
    main()
