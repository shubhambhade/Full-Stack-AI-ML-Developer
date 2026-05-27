# Parent Class
class College:

    def __init__(self, college_name, college_location):
        self.college_name = college_name
        self.college_location = college_location

    def college_rules(self):
        print("\n===== College Rules =====")
        print("1. Maintain 75% attendance")
        print("2. Wear ID card daily")
        print("3. Follow discipline")
        print("4. Submit assignments on time")

    def display_college_information(self):
        print("\nCollege Name :", self.college_name)
        print("College Location :", self.college_location)


# Child Class 1
class ComputerScienceDepartment(College):

    def __init__(self, college_name, college_location, hod_name, total_students):
        super().__init__(college_name, college_location)
        self.hod_name = hod_name
        self.total_students = total_students

    def display_cs_department(self):
        self.display_college_information()

        print("\n--- Computer Science Department ---")
        print("HOD Name :", self.hod_name)
        print("Total Students :", self.total_students)

        self.college_rules()


# Child Class 2
class MechanicalDepartment(College):

    def __init__(self, college_name, college_location, lab_name, total_faculty):
        super().__init__(college_name, college_location)
        self.lab_name = lab_name
        self.total_faculty = total_faculty

    def display_mechanical_department(self):
        self.display_college_information()

        print("\n--- Mechanical Department ---")
        print("Lab Name :", self.lab_name)
        print("Total Faculty :", self.total_faculty)

        self.college_rules()


# Child Class 3
class CivilDepartment(College):

    def __init__(self, college_name, college_location, project_name, total_students):
        super().__init__(college_name, college_location)
        self.project_name = project_name
        self.total_students = total_students

    def display_civil_department(self):
        self.display_college_information()

        print("\n--- Civil Department ---")
        print("Project Name :", self.project_name)
        print("Total Students :", self.total_students)

        self.college_rules()


# Creating Objects

cs = ComputerScienceDepartment(
    "ABC Engineering College",
    "Pune",
    "Dr. Sharma",
    450
)

me = MechanicalDepartment(
    "ABC Engineering College",
    "Pune",
    "Thermal Engineering Lab",
    35
)

civil = CivilDepartment(
    "ABC Engineering College",
    "Pune",
    "Bridge Construction Project",
    300
)


# Calling Methods

cs.display_cs_department()

me.display_mechanical_department()

civil.display_civil_department()