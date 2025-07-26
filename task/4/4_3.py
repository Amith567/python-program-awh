"""
Task 4.3: Student Grade Calculator

Write a function calculate_grades() that:

Accepts a list of student marks for 5 subjects.
Calculates the total, average, and grade
Displays the final result.
"""
lis=[]
print("Enter the score (in 100) : ")
for i in range(5):
    lis.append(int(input("enter the mark : ")))
total=sum(lis)
average=total/5
print(f"Total score : {total}")
print(f"Average score : {average}")
score=average
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
