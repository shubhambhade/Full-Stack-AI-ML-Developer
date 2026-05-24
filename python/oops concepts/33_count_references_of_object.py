import sys

class Test:
    pass

t = Test()
print(sys.getrefcount(t))
