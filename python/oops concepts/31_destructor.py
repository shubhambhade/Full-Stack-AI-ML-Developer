class Student:

    def __init__(self, name):
        self.name = name
        print(f"Constructor called for {self.name}")

    def __del__(self):
        print(f"Destructor called for {self.name}")

s1 = Student("Shubham")
s2 = Student("sham")
s1 = None
s2 =  None
print("end of application")