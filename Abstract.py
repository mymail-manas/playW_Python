from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("Woo")

dog=Dog()
dog.speak()