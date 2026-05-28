class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no = roll_no
        self.marks = marks

    def __str__(self):
        return 'Name : {} , Roll No :{}, Marks : {}'.format(self.name,self.roll_no,self.marks)

s1 = Student("sham",101,89)
s2 = Student("ram",102,90)
print(s1)
print(s2)