class Test:
    def m1(self,x):
        print('{} - argument method'.format(x.__class__.__name__))

t = Test()
t.m1(10)
t.m1(10.45)
t.m1("sham")
t.m1(True)
t.m1([])
t.m1({})
