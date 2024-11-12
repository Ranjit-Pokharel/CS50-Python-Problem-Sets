import inflect

p = inflect.engine()


def main():
    names = []
    while True:
        try:
            # get names for song
            name = input("Input: ")
            names.append(name)
        except EOFError:
            # if ctrl + d then break
            break

    # sing adieu song with names
    sing_adieu(names)


def sing_adieu(names):
    print("\nAdieu, adieu, to", p.join(names))


if __name__ == "__main__":
    main()
