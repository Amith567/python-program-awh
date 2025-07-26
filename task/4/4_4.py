"""
Task 4.4: Find Second Largest Number in a List

Write a function that:

Accepts a list of numbers.
Returns the second-largest number.
"""

lis=[]
print("Enter five numbers : ")
for i in range(5):
    lis.append(int(input()))
lis.sort()
print(f"The second large number in the list is {lis[-2]}")
