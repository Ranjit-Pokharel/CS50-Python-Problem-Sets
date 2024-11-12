import sys, random
from pyfiglet import Figlet

figlet = Figlet()


def main():
    # geting argument excluding the script
    argv = sys.argv[1:]

    # checking program.py [argument] optional valid or not
    error_check(argv)

    # seting the fonts
    if len(argv) == 0:
        figlet.setFont(font=random.choice(figlet.getFonts()))
    else:
        figlet.setFont(font=argv[1])

    # asking user for text
    message = input("Input: ")

    # display text with font
    print("Output:", figlet.renderText(message), sep="\n")


def error_check(argv):
    length = len(argv)

    if length not in [0, 2]:
        sys.exit("Invalid usage")

    if length == 2:
        if argv[0] not in ["-f", "--font"]:
            sys.exit("Invalid usage")
        if argv[1] not in figlet.getFonts():
            sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
