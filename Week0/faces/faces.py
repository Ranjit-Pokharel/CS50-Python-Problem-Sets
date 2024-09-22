def main():
    # ask user for the text
    text = input().strip()

    # display text with converted emoji
    print(faces(text))


def faces(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


if __name__ == "__main__":
    main()