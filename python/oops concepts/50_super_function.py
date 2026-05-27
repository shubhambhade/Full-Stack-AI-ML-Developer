class P:
    def m1(self):
        print('Parent Method')

class C(P):
    def m1(self):
        super().m1()
        print("Child Method")

c = C()
c.m1() 