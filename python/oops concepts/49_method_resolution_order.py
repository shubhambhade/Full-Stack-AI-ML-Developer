class A:pass
class B:pass
class C:pass
class D(A,B):pass
class E(B,C):
    def m1(self):
        print("E class method")
class F(D,E,C):pass

print(A.mro())
print()
print(B.mro())
print()
print(C.mro())
print()
print(D.mro())
print()
print(E.mro())
print()
print(F.mro())
print()
f = F()
f.m1()
