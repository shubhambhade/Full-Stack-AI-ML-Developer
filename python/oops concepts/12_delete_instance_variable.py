class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

    def m1(self):
        #delete inside class 
        del self.c

t = Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
# delete outside of class
del t.d
print(t.__dict__)
# delete multiple elements
del t.a, t.b
print(t.__dict__)