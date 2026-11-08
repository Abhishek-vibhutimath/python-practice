num = int(input("Enter a number: "))
reverse = 0

while num:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(f"Reversed number: {reverse}")

