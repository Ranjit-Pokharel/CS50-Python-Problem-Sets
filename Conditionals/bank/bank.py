"""
pset1/bank
----------
    If the greeting starts with “hello”, output $0.
    If the greeting starts with an “h” (but not “hello”), output $20.
    Otherwise, output $100.
    Ignores any leading whitespace in the user's greeting,
    and treat the user's greeting case-insensitively.
"""

from typing import Literal


def main() -> None:
    """
    bank greet the user

    Parameters
    ----------
        - None

    Returns
    -------
        - None
    """
    # get bank greeting
    bank_greeting: str = input("Greeting: ").lower().strip()

    # check for valid greet
    print(f"${greeting(bank_greeting)}")


def greeting(greet: str) -> Literal[0, 20, 100]:
    """
    determine the greeting amount

    Parameters
    ----------
        - greet (str): greet that is evaluated

    Returns
    -------
        - Literal[0, 20, 100]
            - 0 if greeeting is hello
            - 20 if greeting startwith h
            - 100 gor other types of greeting
    """
    if greet.startswith("hello"):
        return 0
    elif greet.startswith("h"):
        return 20
    return 100


if __name__ == "__main__":
    main()
