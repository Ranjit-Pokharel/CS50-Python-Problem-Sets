def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    print(dollars)
    percent = percent_to_float(input("What percentage would you like to tip? "))
    print(percent)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    return(float(d.replace("$", "")))


def percent_to_float(p):
    # TODO
    return(float(p.replace("%", "")) * 0.01)


main()
