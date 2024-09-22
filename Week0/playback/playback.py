def main():
    ...
    # get quick speaking words 
    quick_speaking = input()

    # slow down speaking and display
    print(slow_down(quick_speaking))


def slow_down(text):
    return text.replace(" ", "...")


main()