class P1:
    def m1(self):
        print("Parent1 method")

class P2:
    def m1(self):
        print("Parent2 method")

class C(P1,P2):
    pass

class D(P2,P1):
    pass

c = C()
c.m1()
print()
d = D()
d.m1()