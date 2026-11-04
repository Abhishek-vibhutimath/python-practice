n = int(input("How many numbers?: "))
l1 = []
even_count = 0
odd_count = 0

for i in range(1,n+1):
    num = int(input(f"Enter number{i}: "))
    l1.append(num)

for i in l1:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
