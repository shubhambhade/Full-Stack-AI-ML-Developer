
class Car:
    def __init__(self,car_name,car_model,car_color):
        self.car_name = car_name
        self.car_model = car_model
        self.car_color = car_color

    def get_information_of_car(self):
        print("Car Name : {}, Car Model : {}, Car Color : {}".format(self.car_name,self.car_model,self.car_color))

class Employee:
    def __init__(self,employee_name, employee_number, car):
        self.employee_name =employee_name
        self.employee_number = employee_number
        self.car = car

    def employee_information(self):
        print("Employee Name : ", self.employee_name)
        print("Employee Number : ",self.employee_number)
        print("Employee Car Info : ")
        self.car.get_information_of_car()

car = Car("bmw","2.5v","red")
employee = Employee("sham",101,car)
employee.employee_information()