"""
pset0/tip
---------
    calculate tip to be given
"""


def main() -> None:
    """
    take dollars amount and tip percent and provide how much tip
    
    Parameters
    ----------
        - (None)
        
    Returns
    -------
        - (None)
    """
    dollars: float = dollars_to_float(input("How much was the meal? "))
    percent: float = percent_to_float(input("What percentage would you like to tip? "))
    tip: float = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    """
    convert the string dollars amount to float
    
    Parameters
    ----------
        - d (str): string dollor amount ($amount)
    
    Returns
    -------
        - (float): converted float
    """
    # TODO
    d = d.replace("$", "")

    return float(d)


def percent_to_float(p: str) -> float:
    """
    convert string percent to float
    
    Parameters
    ----------
        - p (str): string that has percentage e.g 15%
        
    Returns
    -------
        - (float): converted to float
    """
    # TODO
    p = p.replace("%", "")

    return float(p)


if __name__ == "__main__":
    main()