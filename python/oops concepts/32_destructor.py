import time
class Test:
    def __init__(self):
        print("constructor execution")

    def __del__(self):
        print("destructor execution")

t1 = Test()
t2 = t1
t3 = t1
del t1
time.sleep(10)
print("object not destroyed after deleting t1")
del t2
time.sleep(10)
print("object not destroyed even after deleting t2")
print("Removing last reference")
del t3 
print("end of application")
