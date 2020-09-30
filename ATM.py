balance = 10000

while True:

    print("   ATM   ")
    print("""
    1)      Balance
    2)      Withdraw
    3)      Deposit
    4)      Quit
    """)
    try:
        Option=int(input("Enter Option: "))
    except Exception as e:
        print("Error: ", e)
        print("Enter 1, 2, 3 or 4 only")
        continue
    if Option == 1:
        print("Balance $ ",balance)
    if Option == 2:
        print("Balance $ ",balance)
        Withdraw = float(input("Enter Withdraw ammount $"))
        if Withdraw>0 and balance>Withdraw:
            forewardBalance=(balance-Withdraw)
            balance = forewardBalance
            print("Foreward Balance $ ",forewardBalance)
        elif Withdraw>balance:
            print("No funds in account - OPERATION CANCELED")
        else:
            print("None withdraw made")
    if Option == 3:
        print("Balance $ ",balance)
        Deposit=float(input("Enter deposit amount $ "))
        if Deposit > 0:
            forewardBalance=(balance+Deposit)
            balance = forewardBalance
            print("Foreward Balance $ ",forewardBalance)
        else:
            print("None deposit made")
    if Option == 4:
        exit()