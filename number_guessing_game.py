s_num = 99

i = 0

while i<7:
    n = int(input("Guess the number: "))
    if n<s_num:
        print("Too low!")
    elif n>s_num:
        print("Too high!")
    elif n==s_num:
        print("Congratulations! You guessed it!")
        break
    i+=1
else:
    print("Game over! The correct number was 99.")
   