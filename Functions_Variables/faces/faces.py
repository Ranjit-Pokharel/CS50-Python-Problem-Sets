"""
pset0/faces
-----------
    convert emoticons to emoji

Currently, it supports
----------------------
    - :( converted to 🙁
    - :) converted to 🙂
"""


def main() -> None:
    """
    ask user for the text with emoticon and display with emoji

    Parameters
    ----------
        None

    Returns
    -------
        None
    """
    # ask user for the text
    text: str = input().strip()

    # display text with converted emoji
    print(convert(text))


def convert(text: str) -> str:
    """
    convert emoticon to emoji

    Parameters
    ----------
        text (str): text contaning emoticon

    Returns
    -------
        (str): text with emoji
    """
    return text.replace(":)", "🙂").replace(":(", "🙁")


if __name__ == "__main__":
    main()
