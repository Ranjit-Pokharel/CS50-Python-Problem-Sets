def main():
    # ask user for mass
    mass = float(input("m: "))
    
    # print energy
    print(f"E: {energy_calc(mass):.0f}")


def energy_calc(mass):
    c = 300000000
    return mass * c * c


if __name__ == "__main__":
    main()