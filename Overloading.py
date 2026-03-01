class Dog:
    def speak(self):
        print("Voow")
class Cat:
    def speak(self):
        print("Meow")
animals=[Cat(),Dog()]

for animal in animals:
    animal.speak()
