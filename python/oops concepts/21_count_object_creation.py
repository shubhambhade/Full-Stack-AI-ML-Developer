class Test:
    count = 0
    def __init__(self):
        Test.count += 1
    
    @classmethod
    def get_number_of_objects(cls):
        print("The number of objects created : ",cls.count)

Test.get_number_of_objects()
t = Test()
Test.get_number_of_objects()
t1 = Test()
Test.get_number_of_objects()
