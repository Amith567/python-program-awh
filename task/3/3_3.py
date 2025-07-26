"""Task 3.3: Sum of First N Natural Numbers (Using Loops)

Write a program that:

Takes a number N as input.
Uses a for loop to calculate the sum of the first N natural numbers.
Prints the sum.
"""
n=int(input("Enter a number : "))
sum=0
for i in range(n+1):
    sum+=i
    print(i)
print(f"Sum of first {n} is {sum}")