class Person:
    def __init__(self,name,dd,mm,yyyy):
        self.name = name
        self.dob =  self.Dob(dd,mm,yyyy)

    def display(self):
        print(f"Name : {self.name}")
        self.dob.display()
    
    class Dob:
        def __init__(self,dd,mm,yyyy):
            self.dd = dd  
            self.mm = mm  
            self.yyyy = yyyy 
            
        def display(self):
            print('DOB : {}/{}/{}'.format(self.dd,self.mm,self.yyyy))

person = Person("sham patil",24,8,2002)
person.display()