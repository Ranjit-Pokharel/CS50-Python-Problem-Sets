def main():
    # list of month
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    # get valid dates
    day, month, year = get_date("Date: ", months)

    # display in yyyy-mm-dd format
    print(f"{year}-{month:02}-{day:02}")


def get_date(promp, months):
    while True:
        dates = input(promp).strip()
        try:
            if "/" in dates:
                month, day, year = dates.split("/")
                month = int(month)
            elif "," in dates:
                month, day, year = dates.split(" ")
                # given month name is not in the list
                if month not in months:
                    raise ValueError()
                day = day.replace(",", "")

                # find the number of given month
                for i, month_name in enumerate(months):
                    if month.title() == month_name:
                        month = i + 1
                        break
            else:
                continue

            day = int(day)

            if len(year) != 4:
                raise ValueError()
            year = int(year)

            if month > 12:
                raise ValueError()
            if day > 32:
                raise ValueError()
        except ValueError:
            continue

        return (day, month, year)


if __name__ == "__main__":
    main()
