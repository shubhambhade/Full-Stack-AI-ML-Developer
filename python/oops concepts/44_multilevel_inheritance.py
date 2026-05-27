class GrandFather:
    def grandfather_method(self):
        print("Grandfather class")

class Parent(GrandFather):
    def parent_method(self):
        print("Parent class")

class Child(Parent):
    def child_method(self):
        print("Child class")

class ChildChild(Child):
    def child_child_method(self):
        print("ChildChild class")

child_child = ChildChild()
child_child.grandfather_method()
child_child.parent_method()
child_child.child_method()
child_child.child_child_method()
