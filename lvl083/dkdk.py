class Animal:
    def speak(self):
        return "sound"

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __get_age(self):
        return self.__age

    def speak(self):
        return "ruf"

dog = Dog("rebecca", 2)

print(dog.name)
print(dog.speak())