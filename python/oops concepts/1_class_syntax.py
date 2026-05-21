
'''how to define class'''
class calssName:
    '''documentation string (optinal)'''
    # variables : properties/ attributes
    # methods : actions/ behaviours

# Access the document string
print(calssName.__doc__)
help(calssName)

# Example
class Student:
    '''This class developed by shubham for demo'''
    def __init__(self):
        self.name = "sham"
        self.roll_number = 101
        self.marks = 90

    def talk(self):
        print("Hello i am ",self.name)
        print('my roll number is : ',self.roll_number)
        print('my marks are ',self.marks)

# create student class object
s = Student()
print(s.name)
print(s.roll_number)
print(s.marks)
s.talk()