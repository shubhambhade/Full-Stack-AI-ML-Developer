class Car:
    def __init__(self,name, model,color):
        self.name = name
        self.model = model
        self.color = color

    def get_car_info(self):
        print('Car Name : {} \nCar Model : {}\nCar Color : {}'.format(self.name,self.model,self.color))

class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

    def get_person_info(self):
        print("Person Name : ",self.name)
        print("Person Age : ", self.age)

class Employee(Person):
    def __init__(self, name, age,eno,esal,car):
        super().__init__(name,age)
        self.eno = eno
        self.esal = esal 
        self.car = car

    def work(self):
        print("python coding........")

    def emp_info(self):
        super().get_person_info()
        print("Employee Number : ",self.eno)
        print("Employee Salary : ",self.esal)
        print("Employee Car Information")
        self.car.get_car_info()

car = Car("farari","v7","red")
employee =  Employee("sham",34,101,20000,car)
employee.work()
employee.emp_info()