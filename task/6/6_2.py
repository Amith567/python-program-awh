"""
6.2: Constructors in Python

Enhance the Car class:

✔ Use init() to initialize attributes
✔ Accept values from the user and create the object dynamically
✔ Display car details using the method
"""
class car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display(self):
        print(f'brand : {self.brand}\nmodel : {self.model}\nyear : {self.year}')
b=input("enter the brand : ")
m=input("enter the model : ")
y=int(input("enter the year : "))
print("\n")
car_1=car(b,m,y)
car_1.display()