
e_unit = int(input("Enter number of units: "))

if e_unit < 0:
    print("Invalid units")
elif e_unit <= 100:
    bill = e_unit * 2
    print(f"Electricity bill: ₹{bill}")
elif e_unit <= 200:
    bill = (100 * 2) + (e_unit - 100) * 3
    print(f"Electricity bill: ₹{bill}")
else:
    bill = (100 * 2) + (100 * 3) + (e_unit - 200) * 5
    print(f"Electricity bill: ₹{bill}")

