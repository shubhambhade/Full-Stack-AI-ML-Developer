class A:
    def m1(self):
        print("A class method")
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

print(A.mro())
print()
print(B.mro())
print()
print(C.mro())
print()
print(D.mro())

d = D()
d.m1()
