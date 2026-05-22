class Test:
    @staticmethod
    def average(list1):
        result = sum(list1)/len(list1)
        print("The Average : ",result)

    @staticmethod
    def wish(name):
        for i in range(5):
            print("Good Morning ",name)
    
list1 = [10,20,30,40]
Test.average(list1)
Test.wish("shubham")
