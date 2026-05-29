class Person:
    def __init__(self,name ,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def dispaly(self):
        print("Name : ", self.name)
        print("Age : ",self.age)
        print("Height : ",self.height)
        print("Weight : ", self.weight)

class Employee(Person):
    def __init__(self, name, age, height, weight,eno,esal):
        super().__init__(name, age, height, weight)
        self.eno = eno
        self.esal = esal 

    def dispaly(self):
        super().dispaly()
        print("Employee Number : ",self.eno)
        print("Salary : ",self.esal)

e = Employee("sham",23,"162cm","74kg",1011122,22500)
e.dispaly()