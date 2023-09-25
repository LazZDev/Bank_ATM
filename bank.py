balance = 1000


def deposit(amount):
    global balance
    balance += amount
    return True


def withdraw(amount):
    global balance
    if amount > balance:
        return False

    balance -= amount
    return True


def transaction(action):
    if action == 1:
        amount = int(input("Enter the amount you would like to deposit: "))
        return deposit(amount)

    if action == 2:
        amount = int(input("Enter the amount you would like to withdraw: "))
        return withdraw(amount)

    return False


def main():
    global balance
    while True:
        action = int(
            input("What would you like to do? \n1. Deposit\n2. Withdraw\n3. Exit \n\n"))
        if action == 3:
            print("See you later!")
            break

        result = transaction(action)
        if result == False:
            print("This transaction cannot be completed.")
        else:
            print(f"Transaction completed, new balance: {balance}")


main()
