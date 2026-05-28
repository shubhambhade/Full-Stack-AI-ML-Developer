class Test:
    def m1(self, a = None, b = None,c = None):
        if a is not None and b is not None and c is not None:
            print("Three argument method")
        elif a is not None and b is not None:
            print("two argument method")
        elif a is not None:
            print("one argument method")
        else:
            print("no- argument method")

t = Test()
t.m1()
t.m1(10)
t.m1(10,20)
t.m1(10,20,30)
