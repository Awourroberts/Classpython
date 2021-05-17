class Car:
    model="jeep"
    def __init__(self,make,color,registration,speed):
        self.make=make
        self.color=color
        self.regrastration=registration
        self.speed=speed
    def poop(self):
        return f"Hello my color is {self.color}"
        


