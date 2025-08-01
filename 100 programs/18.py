#Python Program to Print the Fibonacci sequence
lis=[]
a=0
b=1
lis.append(a)
lis.append(b)
inp_range=int(input("Enter a number : "))
for i in range(inp_range-2):
    c=a+b
    a=b
    b=c
    lis.append(c)
print(",".join(map(str,lis)))