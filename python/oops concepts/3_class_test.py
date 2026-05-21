class Test : 
    def __init__(self):
        print("The Address of object pointed by self : ",id(self))

t = Test()
print("The Address of object pointed by self : ",id(t))