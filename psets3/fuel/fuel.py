def main():
    # get valid fuel value
    x, y = get_fule_fraction()

    # display Fuel gauges indicate
    print(fuel_lvl(x, y))


def fuel_lvl(x, y):
    fuel = (x / y) * 100
    
    if fuel <= 1:
        return "E"

    if 1 < fuel < 99:
        return f"{round(fuel)}%"

    if 99 <= fuel <= 100:
        return "F"
    


def get_fule_fraction():
    while True:

        fractions = input("Fraction: ")
        
        try:
            fraction_x , fraction_y = fractions.split("/")
            fraction_x, fraction_y= int(fraction_x), int(fraction_y)
        except ValueError:
            continue

        try:
            fraction_x / fraction_y
        except ZeroDivisionError:
            continue

        if fraction_x > fraction_y:
            continue
        
        return fraction_x, fraction_y
    

if __name__ == "__main__":
    main()
