"""
Task 2.3: Operators Practice

Perform operations using:
Arithmetic (+, -, *, /, //, %, **)
Comparison (==, !=, >, <, >=, <=)
Logical (and, or, not)
Assignment (=, +=, -=, *=, etc.)
"""

a=1
b=2
print(f"a : {a}, b : {b}")

print("\nArithmatic operations \n")
print(f"a+b : {a+b}")
print(f"a-b : {a-b}")
print(f"a*b : {a*b}")
print(f"a/b : {a/b}")
print(f"a//b : {a//b}")
print(f"a%b : {a%b}")
print(f"a**b : {a**b}")

print(f"\nComparison operations\n")
print(f"a==b : {a==b}")
print(f"a!=b : {a!=b}")
print(f"a>b : {a>b}")
print(f"a<b : {a<b}")
print(f"a>=b : {a>=b}")
print(f"a<=b : {a<=b}")

print("\nLogical operations\n")
print(f"a and b : {a and b}")
print(f"a or b : {a or b}")
print(f"not a : {not a}")

print("\nAssignment operations\n")
print(f"a=b : {b}")#a=b is not a  f operation, it return error
print(f"a+=b : {a+b}")#a+= ,a-=,a*= will change the value of parent variable
print(f"a-=b : {a-b}")#a+b is same as a+=b
print(f"a*=b : {a*b}")