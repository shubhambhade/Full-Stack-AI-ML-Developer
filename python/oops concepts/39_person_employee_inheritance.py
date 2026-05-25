class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def eat_drink(self):
        print("Eat Briyani")
        print("Drink Beer")

class Employee(Person):
    def __init__(self, name, age, enum, esal):
        # self.name  = name
        # self.age = age
        super().__init__(name,age)
        self.enum = enum
        self.esal = esal

    def work(self):
        print("coding python programs")

    def emp_info(self):
        print(self.name)
        print(self.age)
        print(self.enum)
        print(self.esal)

emp = Employee("sham",34,101,120000)
emp.eat_drink()
emp.work()
emp.emp_info()