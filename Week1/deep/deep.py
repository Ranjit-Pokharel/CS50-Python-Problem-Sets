def main():
    # ask question and get answer
    answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
    # clean user answer
    answer = answer.lower().strip()

    # check for answer
    check = deep_thought(answer)

    # if the user provide correct display yes else no
    if check == True:
        print("Yes")
    else:
        print("No")


def deep_thought(answer):
    answers = ["42", "forty two", "forty-two"]
    if answer in answers:
        return True
    return False


if __name__ == "__main__":
    main()