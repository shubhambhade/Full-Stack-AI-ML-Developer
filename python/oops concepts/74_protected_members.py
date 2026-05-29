class Test:
    def __init__(self):
        self._x = 10
    def m1(self):
        print(self._x)

class SubTest(Test):
    def m2(self):
        print(self._x)

s = SubTest()
s.m1()
s.m2()

# access protected members ouside of class using another ways
print(s._x)
