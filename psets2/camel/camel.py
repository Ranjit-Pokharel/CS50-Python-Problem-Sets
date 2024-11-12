def main():
    # get text in camelCase
    text = input("camelCase: ")

    # convert to snake_case
    converted = to_snake(text)
    print(f"snake_case: {converted}")


def to_snake(camel_string):
    snake_string = ""

    for char in camel_string:
        if char.isupper():
            snake_string += "_" + char.lower()
        else:
            snake_string += char

    return snake_string


if __name__ == "__main__":
    main()
