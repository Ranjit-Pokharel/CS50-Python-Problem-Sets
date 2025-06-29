def main():
    # amount due
    amount_due = 50

    while True:
        # display amount due
        print(f"Amount Due: {amount_due}")

        # ask user for coin
        coin = int(input("Insert Coin: "))

        # check if coin is valid
        if not valid_coin(coin):
            continue

        # calculate amount due and change own
        if amount_due <= coin:
            change_own = change_calc(coin, amount_due)
            print(f"Change Owed: {change_own}")
            break
        else:
            amount_due = change_calc(coin, amount_due)


def valid_coin(coin):
    valid_coins = [25, 10, 5]
    if coin in valid_coins:
        return True
    return False


def change_calc(coin, amount_due):
    return abs(amount_due - coin)


if __name__ == "__main__":
    main()
