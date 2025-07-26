"""
6.5: Polymorphism

Create two classes: Dog and Cat
✔ Both should have a method speak()
✔ Implement polymorphism by calling speak() on both objects via a loop or common function
"""
class Dog:
    def sound(self):
        print("dog : woof ,woof")
class Cat:
    def sound(self):
        print("cat : meow,meow")
dog=Dog()
cat=Cat()
def animal_sound(animal):
    animal.sound()
animals=[dog,cat]
for animal in animals:
    animal_sound(animal)