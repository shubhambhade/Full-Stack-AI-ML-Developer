class Student :

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def set_marks(self, marks):
        self.marks = marks

    def get_marks(self):
        return self.marks

n = int(input("Enter number of student : "))

student = []

for i in range(n):
    s = Student()
    name = input("enter student name : ")
    marks = int(input("enter marks : "))
    s.set_name(name)
    s.set_marks(marks)
    student.append(s)

for s in student:
    print("Hello ", s.get_name())
    print("your marks are : ", s.get_marks())
    print()