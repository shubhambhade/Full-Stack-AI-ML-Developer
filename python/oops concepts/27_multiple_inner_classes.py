# multiple inner classes

class Hospital:
    def __init__(self):
        self.hospital_name = "ruby hall"
        self.den = self.Dentist()
        self.car = self.Cardiologist()

    def show_hospital_detail(self):
        print("Hospital name : ",self.hospital_name)

    class Dentist:
        def __init__(self):
            self.name = "Dr. sham"
            self.degree = "BDS"
        
        def display(self):
            print("Name : ", self.name)
            print("Degree  : ", self.degree)
    
    class Cardiologist:
        def __init__(self):
            self.name = "Dr. ram"
            self.degree = "DM"
        
        def display(self):
            print("Name : ", self.name)
            print("Degree  : ", self.degree)

hospital = Hospital()
hospital.show_hospital_detail()
print()

d = hospital.den 
d.display()

print()

c = hospital.car
c.display()