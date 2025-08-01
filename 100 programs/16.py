#Python Program to Find the Factorial of a Number

def factorial(n):
    
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Enter a number : "))    
result=factorial(5)
print(f"factorial of {n} is {result}")
    