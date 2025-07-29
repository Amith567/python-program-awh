#Python Program to Print all Prime Numbers in an Interval
import math

start=int(input("Enter the starting number : "))
stop=int(input("Enter the ending numer : "))
for i in range(start,stop+1):
    if i<=1:
        print(f"{i} is not a prime number.")
    else:
        is_prime=True
        for j in range(2,int(math.sqrt(i))+1):
            
            if i%j==0:
                is_prime=False
                break
        if is_prime:
                print(f"{i} is a prime number.")
        else:
             print(f"{i} is not a prime number.")
             