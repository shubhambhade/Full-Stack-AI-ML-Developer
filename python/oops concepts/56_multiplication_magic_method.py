class Employee:
    def __init__(self, salary_per_day):
        self.salary_per_day=salary_per_day

    def __mul__(self, other):
        return self.salary_per_day * other.working_days

class TimeSheet:
    def __init__(self,working_days):
        self.working_days = working_days

    def __mul__(self, other):
        return self.working_days * other.salary_per_day

e = Employee(1000)
t = TimeSheet(30)
print("This month salary : ", e*t)
print("This month salary : ", t*e)

#order of object important here