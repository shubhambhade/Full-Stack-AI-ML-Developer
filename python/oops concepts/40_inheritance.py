# Parent Class
class Vehicle:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def start(self):
        print(f"{self.brand} Vehicle Started")

    def stop(self):
        print(f"{self.brand} Vehicle Stopped")

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.speed} km/h")


# Child Class
class Car(Vehicle):

    def __init__(self, brand, speed, wheels):
        super().__init__(brand, speed)
        self.wheels = wheels

    def honk(self):
        print(f"{self.brand} Car Honking...")

    def display_info(self):
        super().display_info()
        print(f"Wheels: {self.wheels}")


# SportsCar Class
class SportsCar(Car):

    def turbo_mode(self):
        print(f"{self.brand} Turbo Mode Activated ")

    def display_info(self):
        super().display_info()
        print("Type: Sports Car")


# ElectricCar Class
class ElectricCar(Car):

    def __init__(self, brand, speed, wheels, battery):
        super().__init__(brand, speed, wheels)
        self.battery = battery

    def charge(self):
        print(f"{self.brand} Battery Charging ")

    def display_info(self):
        super().display_info()
        print(f"Battery: {self.battery} kWh")


# Tesla Class (Multilevel Inheritance)
class Tesla(ElectricCar):

    def autopilot(self):
        print("Tesla AutoPilot Enabled ")

    def display_info(self):
        super().display_info()
        print("Model: Tesla")


# SUV Class
class SUV(Car):

    def offroad(self):
        print(f"{self.brand} Off-Road Mode Enabled ")

    def display_info(self):
        super().display_info()
        print("Type: SUV")


# LuxuryCar Class
class LuxuryCar(Car):

    def massage_seats(self):
        print(f"{self.brand} Massage Seats Activated ")

    def display_info(self):
        super().display_info()
        print("Type: Luxury Car")


# Main Program
print("===== TESLA =====")

tesla = Tesla("Tesla", 250, 4, 100)

tesla.start()
tesla.honk()
tesla.charge()
tesla.autopilot()
tesla.display_info()

print("\n===== SPORTS CAR =====")

ferrari = SportsCar("Ferrari", 320, 4)

ferrari.start()
ferrari.turbo_mode()
ferrari.display_info()

print("\n===== SUV =====")

fortuner = SUV("Toyota Fortuner", 180, 4)

fortuner.start()
fortuner.offroad()
fortuner.display_info()

print("\n===== LUXURY CAR =====")

bmw = LuxuryCar("BMW", 240, 4)

bmw.start()
bmw.massage_seats()
bmw.display_info()