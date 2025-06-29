"""
pset0/indoor

displey inputed text entirely in lowercase

"""


def main() -> None:
    """
    ask user for input of text and print lowercase text

    Parameters
    -----------
        None

    Returns
    --------
        None
    """
    # get text in uppercase
    text: str = input()

    # say text in lowercase
    print(indoor_voice(text))


def indoor_voice(text: str) -> str:
    """
    convert the text all letters to lowercase

    Parameters
    ----------
        text (str): the text that is to be converted to lowercase

    Returms
    -------
        str: all lowercase text
    """
    return text.lower()


if __name__ == "__main__":
    main()
