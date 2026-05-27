#composition
class University:
    def __init__(self):
        self.dept = self.Department()

    class Department():
        pass

university = University()


# Aggregation
class Professor:
    pass
class Department:
    def __init__(self,professor):
        self.professor = professor

professor = Professor()
computer_science_department = Department(professor)
it_department = Department(professor)
