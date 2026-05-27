class P:
    a = 10
    def __init__(self):
        print("Parent constructor")

    def m1(self):
        print("Parent instance method")

    @classmethod
    def m2(cls):
        print("parent Class method")

    @staticmethod
    def m3():
        print("parent static method")

class C(P):
    def __init__(self):
        print("child constructor")
    def m1(self):
        print(super().a)
        super().m1()
        super().m2()
        super().m3()
        super(). __init__()

c = C()
c.m1()