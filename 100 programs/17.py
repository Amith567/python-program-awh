#Python Program to Display the multiplication Table

user_inp=int(input("Enter the number : "))
for n in range(1,11):
    print(f"{n} X {user_inp} = {n*user_inp}")