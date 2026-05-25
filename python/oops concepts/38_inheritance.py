class Parent:
    num = 10
    def __init__(self):
        print("parent class constructor")
        self.num1 = 80
    
    def parent_instance_method(self):
        print("parent instance method")

    @classmethod
    def parent_class_method(cls):
        print("parent class method")
    
    @staticmethod
    def parent_static_method():
        print("parent static method")
    
class Child(Parent):
    pass

child = Child()
print(child.num)
print(child.num1)
child.parent_instance_method()
child.parent_class_method()
child.parent_static_method()
