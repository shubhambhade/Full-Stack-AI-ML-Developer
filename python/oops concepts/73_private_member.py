class Test:
    def __init__(self):
        self.__x = 10
    
    def __m1(self):
        print("private members")

    def m2(self):
        print(self.__x)
        self.__m1()

t = Test()
t.m2()

# no access because of private members
# print(t.__x)
# t.__m1()

'''Another way to access'''
print(t._Test__x)
t._Test__m1()