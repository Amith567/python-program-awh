"""
 Task 3.1: Even or Odd Checker

Write a Python program that:

Takes an integer as input.
Uses an if-else statement to check if the number is even or odd.
Prints the result.
"""
def oddoreven(inp):
    return "Even"if inp%2==0 else "Odd"
inp=int(input("Enter a integer : "))
print(f"{inp} is : {oddoreven(inp)}")