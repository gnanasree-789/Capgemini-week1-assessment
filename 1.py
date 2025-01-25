balance=int(input("Enter the balance: "))
def check_balance(balance):
    print(f"old balance:{balance}")
def deposit_money(balance):
    amount=int(input("Enter amount to deposit: "))
    balance+=amount
    print(f"present balance after deposit:{balance}")
def withdraw_money(balance):
    amount=int(input("Enter amount to withdraw: "))
    if amount<=balance:
        balance-=amount
        print(f"present balance after withdraw:{balance}")
    else:
        print("Insufficient balance for withdraw")
check_balance(balance)
deposit_money(balance)
withdraw_money(balance)