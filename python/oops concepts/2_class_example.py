
#  dynamic data taking 
class Student:
    def __init__(self, name, roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_student_information(self):
        print("Student name : ",self.name)
        print("Student roll number : ", self.roll_number)
        print("Student marks : ",self.marks)

s1 = Student("sham",101,89)
s2 = Student("ram",102,98)
s1.display_student_information()
s2.display_student_information()