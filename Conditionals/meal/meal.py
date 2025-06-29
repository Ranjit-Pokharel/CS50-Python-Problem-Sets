"""
psets1/meal
-----------
    a program that prompts the user for a time
    and outputs whether it's breakfast time,
    lunch time, or dinner time.
    If it's not time for a meal,
    don't output anything at all.

Formatted
---------
    in 24-hour time as #:## or ##:##.
    And assume that each meal's time range is inclusive.
    For instance, whether it's 7:00, 7:01, 7:59, or 8:00,
    or anytime in between, it's time for breakfast.
"""


def main() -> None:
    """
    get time from user and evaluate the time
    if dinner or lunch or breakfast

    Parameters
    ----------
    - None

    Returns
    -------
    - None
    """
    # ask user for time
    time: str = input("What time is it? ")

    # convert the time
    hours = convert(time)

    # check time to display the meal type
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")


def convert(time: str) -> float:
    """
    evaluate the time provided

    Parameters
    ----------
    - time (str):
        the time that need evaluation

    Returns
    -------
    - float: result after evaluation
    """
    hrs, min = time.split(":")

    if "a.m" in min:
        min, _ = min.split(" ")

    if "p.m" in min:
        min, _ = min.split(" ")
        hrs = str(12 + float(hrs))

    min = float(min) / 60
    return float(hrs) + min


if __name__ == "__main__":
    main()
