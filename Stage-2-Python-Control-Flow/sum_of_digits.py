num = int(input("Enter a number: "))
l1 = []

while num:
    i=num%10
    l1.append(i)
    j=num//10
    num=j
print(l1)
print(sum(l1))



