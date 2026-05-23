
class Employee:
    def __init__(self, employee_number, employee_name, employee_salary):
        self.employee_number = employee_number
        self.employee_name = employee_name
        self.employee_salary = employee_salary

    def display_employee_information(self):
        print("Employee Number : ",self.employee_number)
        print("Employee Name : ",self.employee_name)
        print("Employee Salary : ",self.employee_salary)
    
class Manager:
    def update_employee_salary(employee):
        employee.employee_salary += 10000
        employee.display_employee_information()

employee = Employee(101,'sham',45000)
Manager.update_employee_salary(employee)