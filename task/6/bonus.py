"""
 Bonus Challenge – Student Management System
Build a small OOP-based app that:
✔ Allows storing and managing student records
✔ Uses classes and inheritance
✔ Has methods for adding, displaying, and removing student data
"""
class Person:
    def __init__(self,names,age):
        self.names=names
        self.age=age
    def display_info(self):
        return f"name : {self.names} \nage : {self.age}\n"
    
class Student(Person):
    def __init__(self, names, age,id):
        super().__init__(names, age)
        self.id=id
    def display_id(self):
        return f"{super().display_info()}id : {self.id}"

class Studentmanager:
    def __init__(self):
        self.students=[]

    def add_student(self,names,age,id):
        print("*"*30)
        student=Student(names,age,id)
        self.students.append(student)
        print(f"\nstudent added :\n\n{student.display_id()}")
        

    def display_all(self):
        print("*"*30)
        print("\ndisplay all students deatails\n")
        if not self.students:
            print("no data found")
        for student in self.students:
            print(student.display_id())
            print()
    def remove_student(self,id):
        print("*"*30)
        for student in self.students:
            if student.id==id:
                self.students.remove(student)
                print(f"removed \n\n{student.display_id()}")
            
        return f"no student exist with id :{id}"

manager = Studentmanager()
manager.add_student("Anaya", 20, "STU001")
manager.add_student("Raj", 22, "STU002")
manager.display_all()
manager.remove_student("STU001")
manager.display_all()




