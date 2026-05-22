class Test :
    # within class directly, but outside any method
    a = 10
    def __init__(self):
        #inside constructor by using class name
        Test.b = 20
    
    def m1(self):
        #inside instance method by using class name
        Test.c = 30

    @classmethod
    def m2(cls):
        #inside class method by using cls or class name
        cls.d = 40
        Test.e = 50
    @staticmethod
    def m3():
        # inside static method by using class name
        Test.f = 60

t = Test()
print(Test.__dict__)
t.m1()
Test.m2()
t.m3()
# outside of class by using class name
Test.g = 70
print(Test.__dict__)
