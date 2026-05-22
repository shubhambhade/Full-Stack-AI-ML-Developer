class Bird:
    wings = 2
    @classmethod
    def fly(cls, name):
        print(f'{name} flying with {cls.wings} wings')

Bird.fly("Egal")
Bird.fly("Parrot")