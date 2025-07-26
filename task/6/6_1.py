"""
 Task 6.1: Class and Object Creation

Create a class Car with:

✔ Attributes: brand, model, year
✔ A method display_details() that prints the car's information
✔ Create two objects of the Car class and display their details
"""
class car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def display(self):
        print(f"brand : {self.brand}\nmodel : {self.model}\nyear : {self.year}\n")        
    
car_1=car("bens","c",2000)
car_1.display()
car_2=car("maruti","wagnor",2015)
car_2.display()