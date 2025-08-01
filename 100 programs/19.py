#Python Program to Check Armstrong Number

inp=int(input("Enter a number : "))
strin=str(inp)
temp=0
for i in strin:
    temp+=(int(i)**(len(strin)))
if inp==temp:
    print(f"{inp} is armstrong")
else:
    print(f"{inp} isn't armstrong")
