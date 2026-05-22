class Test:
    a = 10
    b = 20
    c = 30
    @classmethod
    def m1(cls):
        del Test.a
        del cls.b 

print(Test.__dict__)
Test.m1()
del Test.c
print(Test.__dict__)
