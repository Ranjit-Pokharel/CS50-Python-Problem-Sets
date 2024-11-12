def main():
    # get expression
    expression = input("Expression: ")

    # interprete the expression
    answer = math_interpreter(expression)

    # display answer
    print(f"{answer:.1f}")


def math_interpreter(expression):
    return eval(expression)


if __name__ == "__main__":
    main()
