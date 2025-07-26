"""Task 2.4: Mini Challenge – Build a Simple Calculator

🛠 Write a Python program that:

Takes two numbers as input.
Performs all arithmetic operations and displays results.
📌 Hint: Use input() to get user values and float() for conversion.
"""
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return "division by zero isn't allowed" if b==0 else a/b
def mul(a,b):
    return a*b

op_1=float(input("Enter first operand : "))
op_2=float(input("Enter second operand : "))
print("\nOperations")
print("1.Addition\n2.Subtraction\n3.Division\n4.Multiplication\n5.Exit\n")
choice=int(input("Enter your choice : "))
if choice==1:
    print(f"a+b :{add(op_1,op_2)}")
elif choice==2:
    print(f"a-b : {sub(op_1,op_2)}")
elif choice==3:
    print(f"a/b : {div(op_1,op_2)}")
elif choice==4:
    print(f"a*b : {mul(op_1,op_2)} ")
elif choice==5:
    exit()
else:
    print("Invalid input !,Enter it again.")