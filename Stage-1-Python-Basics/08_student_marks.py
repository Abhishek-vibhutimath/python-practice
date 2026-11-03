s_name = input("Enter student name:")
total_m = 500
t_marks = 0
valid = True

print("Enter marks for 5 subject:")



for i in range(1,6):
    marks = int(input(f"Subject {i}: "))
    if 0 <= marks <= 100:
        t_marks += marks
    else:
        print("Invalid marks")
        valid = False
        break

if valid:
    percentage = float(t_marks/total_m*100)
    print(f"Student name: {s_name}")
    print(f"Total marks: {t_marks}")
    print(f"Percentage: {percentage}%")

    if 90 <= percentage <= 100:
        print("Grade: A")
    elif 80 <= percentage < 90:
        print("Grade: B")
    elif 70 <= percentage < 80:
        print("Grade: C")
    elif 60 <= percentage < 70:
        print("Grade: D")
    else:
        print("Fail")
else:
    print("Please enter valid marks.")
    
