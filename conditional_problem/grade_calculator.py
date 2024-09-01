# Assign a letter grade based on a student's score A(90-100), B(80-89), C(70-79), D(60-69), F(bellow 60).

marks = int(input("Enter marks : "))

if marks >100:
    print("Check Your grade and try again!")
    exit()
if marks > 90 and marks <= 100:
    print("A grade")

elif marks >80 and marks < 89:
    print("B grade")

elif marks >70 and marks < 79:
    print("C grade")

elif marks >60 and marks < 69:
    print("D grade")
else:
    print("F")