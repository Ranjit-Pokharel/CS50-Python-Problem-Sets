"""
psets1/interpreter
------------------
    program that prompts the user for an arithmetic expression 
    and then calculates and outputs the result as a floating-point value 
Formatted
---------
    x y z 
    with one space between x and y and one space between y and z
    - x is an integer
    - y is +, -, *, or /
    - z is an integer
"""


def main() -> None:
    """
    get the math expression and print result

    Parameters
    ----------
    - None

    Returns
    -------
    - None
    """
    # get expression
    expression: str = input("Expression: ")

    # interprete the expression
    answer: int = math_interpreter(expression)

    # display answer
    print(f"{answer:.1f}")


def math_interpreter(expression: str) -> int:
    """
    evaluate the math expression and gives result

    Parameters
    ----------
    - extression (str):
        the math expression that is to be evaluated

    Returns
    -------
    - int: result after evaluation
    """
    return eval(expression)


if __name__ == "__main__":
    main()
