class Test:
    def sum(self,*args):
        total = 0
        for ele in args:
            total += ele
        print("The Sum : ", total)

t = Test()
t.sum()
t.sum(10)
t.sum(10,20)
t.sum(10,20,30)
t.sum(10,20,30,30,40,50,60,70,60)
