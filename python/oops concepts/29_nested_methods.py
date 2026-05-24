class Test: 
    def m1(self):
        def cal(a,b):
            print("The sum : ", a+b)
            print("The difference : ", a-b)
            print("The product : ", a*b)
            print("The average : ", (a+b)/2)

        cal(10,20)
        print()
        cal(100,20)

t = Test()
t.m1()