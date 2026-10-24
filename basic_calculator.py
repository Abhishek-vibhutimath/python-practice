num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
task = input("Enter operation,(+,-,*,/): ")

if task=="+":
    print(f"sum: {num1+num2}")
elif task=="-":
    print(f"difference: {num1-num2}")
elif task=="*":
    print(f"Product: {num1*num2}")
elif task=="/":
    if num2==0:
        print("Cannot divide by zero")
    else:
        print(f"Quotient: {num1/num2}")
else:
    print("Invalid operation. Choose +, -, *, or /.")


