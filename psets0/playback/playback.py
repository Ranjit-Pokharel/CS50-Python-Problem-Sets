"""
pset0/payback

put ``...`` inbetween the words replacing space (" ")
"""


def main() -> None:
    """
    get quick speaking word from user

    Parameters
    ----------
        None

    Returns
    -------
        None
    """
    # get quick speaking words from user 
    speaking_quickly: str = input()

    # slow down speaking and display
    print(slow_down(speaking_quickly))


def slow_down(text: str) -> str:
    """
    replace space in with (...)
    
    Parameters
    ----------
        text (str): text which has space
        
    Returns
    -------
        str: text whose space is converted to (...)
    """
    return text.replace(" ", "...")


if __name__ == "__main__":
    main()