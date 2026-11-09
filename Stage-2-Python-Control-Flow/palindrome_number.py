num = int(input("Enter a number: "))
original = num
l1 = 0

while num:
    i  = num%10
    l1 = l1*10+i
    num = num//10
   
if l1==original:
    print("Palindrome")
else:
    print("Not a palindrome")