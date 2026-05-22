class Student:
    school_name = "svpm"
    def __init__(self,name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # instance method
    def get_student_info(self):
        print("Student name : ", self.name)
        print("Student roll no : ",self.roll_no)

    # class method 
    @classmethod  
    def school_info(cls):
        print("Student school name : ", cls.school_name)
    
    #static method
    @staticmethod
    def get_sum(a, b):
        return a + b
