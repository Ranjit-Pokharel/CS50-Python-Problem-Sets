"""
pset0/einstein
--------------
    program that prompts the user for mass as an integer (in kilograms) 
    and then outputs the equivalent number of Joules as an integer

Use
---
    E = mc^2
    c = 300000000
"""


def main() -> None:
    """
    ask user for the mass and calculate the joules

    Parameters
    ----------
        None

    Returns
    -------
        None
    """
    # ask user for mass
    mass: int = int(input("m: "))

    energy = equivalent(mass)
    # print energy
    print(f"E: {energy}")


def equivalent(mass: int, c: int = 300000000) -> int:
    """
    using E = mc^2 convert mass to energy

    Parameters
    ----------
        - mass (int): mass in kg to be converted to energy
        - c (int) (default = 300000000): predefined speed default 300000000

    Returns
    -------
        result (int): result of E = mc^2
    """
    result: int = mass * pow(c, 2)
    return result


if __name__ == "__main__":
    main()
