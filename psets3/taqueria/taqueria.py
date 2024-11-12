def main():
    # menu of entrees
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # initial total
    total = 0

    while True:
        # get item that is in menu
        item = get_item(menu)

        if item == None:
            continue
        
        # adding price of items
        total += menu[item]

        # display total
        print(f"${total:.2f}")


def get_item(menu):
        
        try:
            item = input("Item: ").title()
        except EOFError:
            quit()

        if item not in menu:
            return None
        
        return item
        

if __name__ == "__main__":
    main()