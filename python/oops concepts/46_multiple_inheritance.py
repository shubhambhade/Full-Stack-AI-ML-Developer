class Father:
    def house(self):
        print("Father has house")

class Mother:
    def jewelry(self):
        print("Mother has jewelry")

class Child(Father, Mother):
    def car(self):
        print("Child has car")

child = Child()

child.house()
child.jewelry()
child.car()