def main():
    # ask user for time
    time = input("What time is it? ")

    # convert the time
    hours = convert(time)

    # check time to display the meal type
    if hours >= 7 and hours <= 8:
        print("breakfast time")
    elif hours >= 12 and hours <= 13:
        print("lunch time")
    elif hours >= 18 and hours <= 19:
        print("dinner time")


def convert(time):
    hrs, min = time.split(":")
    
    if "a.m" in min:
        min , _ = min.split(" ")
    
    if "p.m" in min:
        min, _ = min.split(" ")
        hrs = str(12 + float(hrs))
    
    min = float(min) / 60
    return(float(hrs) + min)


if __name__ == "__main__":
    main()
