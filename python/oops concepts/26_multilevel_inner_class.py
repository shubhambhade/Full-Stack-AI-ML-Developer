# nesting inner classes - multilevel inner classes
class Outer : 
    def __init__(self):
        print("outer class object creation")

    class Inner:
        def __init__(self):
            print("Inner class object creation")

        class InnerInner():
            def __init__(self):
                print("inner inner class object creation")
            
            def m1(self):
                print("nested inner class method")

Outer().Inner().InnerInner().m1()