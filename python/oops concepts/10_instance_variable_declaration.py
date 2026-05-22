
class Test : 
    def __init__(self):
        # declare inside constructor by using self
        self.a = 10
        self.b = 20
    def m1(self):
        #declare inside instance method by using self
        self.c = 30

t = Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
# declare using object reference
t.d  = 40
print(t.__dict__)
