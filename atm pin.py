pin=9631
pin1=int(input("Enter your pin: "))
if pin1==pin:
    print("Withdrawal amount and Check balance")
    enter=input("Enter W for withdrawal and C for check balance: ")
    if enter=='C' or enter=='c':
        print("Current balance: 10000")
    elif enter=='W' or enter=='w':
        print("Withdrawal amount")
    amount=int(input("Enter the amount to withdraw: "))
    if amount<=10000:
        print(f"Current balance: {10000 - amount}")
    else:
        print(f"Your balance is low amount : 10000")
elif pin1!=pin:
    print("Invalid pin")
    print("Try again or forgot pin?")