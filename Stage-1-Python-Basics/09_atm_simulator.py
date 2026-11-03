
pin = int(input("Enter pin code: "))
w_amount = int(input("Enter withdrawal amount: "))
min_balance = 10000

if w_amount <= 0:
    print("Withdrawal amount must be positive")

elif w_amount > min_balance:
    print("Insufficient balance")

elif w_amount % 100 != 0:
    print("Withdrawal amount must be a multiple of 100")

else:
    r_balance = min_balance - w_amount
    print("Withdrawal successful!")
    print(f"Remaining balance: {r_balance}")



