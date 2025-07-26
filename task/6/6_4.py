""" 
6.4: Inheritance

Create two classes:

Person with name and age

Student inheriting from Person with additional attribute student_id

✔ Use constructors in both classes
✔ Create an object of Student and call methods from both classes
"""
class person:
    def __init__(self,names,age):
        self.names=names
        self.age=age
    def display_info(self):
        print(f"name : {self.names}\nage : {self.age}")

class student(person):
    def __init__(self, names, age,id):
        super().__init__(names, age)
        self.id=id
    def display_id(self):
        print(f"id : {self.id}")
        



person_1=student("amith",20,9)
person_1.display_info()
person_1.display_id()