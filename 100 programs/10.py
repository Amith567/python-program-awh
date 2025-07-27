#Python Program to Check if a Number is Positive, Negative or 0

inp=int(input("enter a numer : "))
if inp==0:
    print(f"{inp} is Zero")
elif inp<0:
    print(f"{inp} is negative")
else:
    print(f"{inp} is positive")