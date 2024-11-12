def main():
    # ask for text from user
    text = input("Input: ")

    # display text without vowels
    print(del_vowels(text))


def del_vowels(text):
    vowels = set("aeiouAEIOU")
    no_vowel = []
    # remove vowels if text char is vowels
    for ch in text:
        if ch not in vowels:
            no_vowel.append(ch)
    return "".join(no_vowel)


if __name__ == "__main__":
    main()
