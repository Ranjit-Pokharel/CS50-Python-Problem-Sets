def main():
    # get bank greeting
    bank_greet = input("Greeting: ").lower().strip()

    # check for valid greet
    print(f"${greeting(bank_greet)}")


def greeting(greet):
    if greet.startswith("hello"):
        return 0
    elif greet.startswith("h"):
        return 20
    return 100


if __name__ == "__main__":
    main()