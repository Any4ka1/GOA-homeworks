balance = 10  # Anna starts with 10 lari

amount = int(input("Enter amount to pay: "))  # Ask how much to pay

if amount > balance:
    print("You don't have enough balance!")
elif amount == 5:
    balance -= 5
    print("Bought an apple")
elif amount == 2:
    balance -= 2
    print("Bought a pear")
else:
    print("Can only buy apples (5 lari) or pears (2 lari)")