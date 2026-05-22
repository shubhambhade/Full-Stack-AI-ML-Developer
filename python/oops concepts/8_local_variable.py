
class Student:
    school_name = "svpm" # static variable
    def __init__(self, name, roll_no):
        # instance variables
        self.name = name
        self.roll_no =  roll_no

    def info(self):
        x = 10 # local variable
        for i in range(x): # i is local variable
            print(i)