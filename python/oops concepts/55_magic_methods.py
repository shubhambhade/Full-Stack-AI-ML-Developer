class Student: 
    def __init__(self,marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks
    
    def __lt__(self, other):
        return self.marks < other.marks
    
    def __eq__(self, value):
        return self.marks == value.marks
    
    def __le__(self, other):
        return self.marks <= other.marks
    
    def __ge__(self, other):
        return self.marks >= other.marks

s1= Student(67)
s2= Student(90)
print(s1>s2)
print(s1<s2)
print(s1 == s2)
print(s1 <= s2)
print(s1 >= s2)