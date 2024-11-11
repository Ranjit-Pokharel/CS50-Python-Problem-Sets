import random


def main():
    level = get_level("Level: ")

    number = get_number(level)

    guess_number(number)

def get_level(promp):
    while True:
        try:
            level = int(input(promp))
            if level < 1: raise ValueError
            return level
        except ValueError:
            continue

def get_number(level):
    return random.randint(1, level)

def guess_number(number):
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue

        if guess > number:
            print("Too Large!")
        elif guess < number:
            print("Too small!")
        else:
            print("Just Right!")
            break


if __name__ == "__main__":
    main()
