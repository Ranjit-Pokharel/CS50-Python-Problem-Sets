"""
pset1/deep
----------
    ask the user for the answer
    to the Great Question of life, the universe
    and Everything.
"""


def main() -> None:
    """
    ask user for answer and if true response as yes else no

    Parameters
    ----------
        - None

    Returns
    -------
        - None
    """

    # ask question to user and get the answer
    answer: str = input(
        "What is the Answer to the Great Question of Life, the Universe and Everything? "
    )

    # clean user answer
    answer = answer.lower().strip()

    # check for answer
    is_valid: bool = is_deep_thought_valid(answer)

    # if the user provide correct answer print yes else no
    if is_valid:
        print("Yes")
    else:
        print("No")


def is_deep_thought_valid(
    answer: str, answers: list = ["42", "forty two", "forty-two"]
) -> bool:
    """
    check if the given answer to the question is true or not

    Parameters
    ----------
        - answer (str): the provided answer to be check
        - answers (list) (default=["42", "forty two", "forty-two"]): the answers that are valid
    Returns
    -------
        - bool: true or false
    """
    if answer in answers:
        return True
    return False


if __name__ == "__main__":
    main()
