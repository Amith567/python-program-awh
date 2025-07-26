"""
Task 3.2: Grading System

Write a program that:

Takes a student's score as input.
Uses an if-elif-else structure to assign grades:
90+ → A
80-89 → B
70-79 → C
60-69 → D
Below 60 → F
Prints the grade.
"""
score=int(input("Enter the score : "))
if score>90:
    print("A grade")
elif score>=80:
    print("B grade")
elif score>=70:
    print("C grade")
elif score>=60:
    print("D grade")
else:
    print("F grade")