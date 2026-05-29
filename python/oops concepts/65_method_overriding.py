class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog Barks")

dog = Dog()
dog.sound()