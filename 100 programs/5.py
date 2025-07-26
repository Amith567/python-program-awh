#Python Program to Solve Quadratic Equation

a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))
sec1=b**2 -4*a*c
sec2=sec1**2

root1=-b+sec2/(2*a)
root2=-b-sec2/(2*a)
print(f"-b+ (b2 4ac)/2a) : {root1}")
print(f"-b- (b2 4ac)/2a : {root2}")


