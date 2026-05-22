class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("hi ", self.name)
        print("your marks are : ", self.marks)
    
    def grade(self):
        if self.marks >= 60:
            print("your got first grade")
        elif self.marks >= 50:
            print("you got second grade")
        elif self.marks >= 35:
            print("you got third grade")
        else:
            print("you are failed")

number_of_student = int(input("Enter no of student : "))

for i in range(number_of_student):
    name = input("Enter student name : ")
    marks = int(input("Enter marks : "))
    student = Student(name, marks)
    student.display()
    student.grade()
    print()