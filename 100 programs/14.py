#Python Program to Check Prime Number
import math
inp=int(input("Enter a number : "))
if inp<=1:
    print(f"{inp} is not a prime number.")
else:
    for i in range(2,int(math.sqrt(inp))+1):
        if inp%i==0:
            print(f"{inp} is not a prime number.")
            break
        else:
            print(f"{inp} is a prime number.")