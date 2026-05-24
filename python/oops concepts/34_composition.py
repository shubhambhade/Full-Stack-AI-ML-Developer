class Engine:
    def __init__(self):
        self.power = '123kw'

    def use_engine(self):
        print("engine specific functionality")

class Car:
    def __init__(self):
        self.engine = Engine()
    
    def use_car(self):
        print("car required engine functionality")
        self.engine.use_engine()
        print(self.engine.power)

car = Car()
car.use_car()

