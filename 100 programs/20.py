#Python Program to Find Armstrong Number in an Interval
start=int(input("enter starting number : "))
end=int(input("enter the ending number : "))
lis=[]
for i in range(start,end+1):
    res=0
    k=str(i)
    for digi in str(i):
        res+=int(digi)**len(k)
    if res==i:
        lis.append(i)
print(f"Armstrong numbers in range {start} to {end} are: {', '.join(map(str, lis))}")

