class Parent:
    def __init__(self):
        print("Parent constructor")
    
    def m1(self):
        print("parent instance method")
    
    @classmethod
    def m2(cls):
        print("parent classs method")
    
    @staticmethod
    def m3():
        print("parent static method")

class Child(Parent):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    @classmethod
    def m2(cls):
        # invalid constructor and instance method call here
        # super().__init__()
        # super().m1()

        # indirect way
        super(Child,cls).__init__(cls)
        super(Child,cls).m1(cls)

        super().m2()
        super().m3()
    @staticmethod
    def m3():
        # all things are invalid
        # super().__init__()
        # super().m1()
        # super().m2()
        # super().m3()
        super(Child,Child).m2()
        super(Child,Child).m3()

child = Child()
print()
child.m1()
print()
Child.m2()
print()
Child.m3()