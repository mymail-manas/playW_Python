class Animal:
    def speaks(self):
        print("Animal speaks")

class Dog(Animal):
    a=12
    #def speaks(self):
    #   print("Dog barks")

Dog1=Dog()
Dog1.speaks()
    
class Car:
    def __init__(self,brands,speeds):
        self.__brand=brands
        self.__speed=speeds

    def get_speed(self):
        return self.__speed
    def get_brand(self):
        return self.__brand
    
Cars1=Car("Hyndai",100)
print(Cars1.get_speed())
print(Cars1.get_brand())


