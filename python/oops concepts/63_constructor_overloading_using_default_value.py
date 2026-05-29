class Test:
    def __init__(self, a = None, B = None, c = None):
        print("constructor with 0|1|2|3 arguments")

t = Test()
t = Test(10)
t = Test(10,20)
t = Test(10,20,30)