class Parent:
    def parent_method(self):
        print("Parent class method")

class Child(Parent):
    def child_method(self):
        print("Child class method")

child = Child()
child.parent_method()
child.child_method()