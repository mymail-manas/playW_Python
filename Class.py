class Car:
    Wheel=4
    def __init__(self,brand,modelname):
        self.brand=brand
        self.model=modelname
        
    def Display_Info(self):
        print (f"{self.brand}{self.model} has {self.Wheel} Wheels")

object1=Car("Maruti","Baleno")
object1.Display_Info()
    