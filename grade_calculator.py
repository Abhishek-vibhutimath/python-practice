marks = int(input("Enter marks: "))

if 90<= marks <=100:
    print("Grade: A")
elif 80<= marks <=89:
    print("Grade: B")
elif 70<= marks <=79:
    print("Grade: C")
elif 60<= marks <=69:
    print("Grade: D")
elif 40<= marks <=59:
    print("Grade: E")
elif 0<= marks <40:
    print("Fail")
else:
    print("Invalid marks")
