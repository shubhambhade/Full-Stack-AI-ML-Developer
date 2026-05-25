class Parent:
    def parent_class_method(self):
        print("parent class method")

class Child(Parent):
    def child_class_method(self):
        print("child class method")

child = Child()
child.parent_class_method()
child.child_class_method()
