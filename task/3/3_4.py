"""Task 3.4: Print Multiplication Table (Using Loops)

Write a program that:

Takes an integer input N.
Uses a for loop to print the multiplication table of N (from 1 to 10)
"""
n=int(input("Enter a number : "))
for i in range(10):
    print(f"{i+1} x {n} : {(i+1)*n}")