p_amount = float(input("Enter principle amount: "))
interest = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time in year: "))

simple_interest = (p_amount*interest*time)/100
total_amount = p_amount + simple_interest
print(f"Simple Interest: {simple_interest}")
print(f"Total Amount is: {total_amount}")

# '''
# This is the simple interest calculator code 
# which can calculate simple interest ,
# provided all required inputs are entered

# '''