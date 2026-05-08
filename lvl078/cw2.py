class Myclass:
    a = 86
class Animal:
    def __init__(self, name, age, jeision_born, color):
        self.name = name
        self.age = age
        self.jeision_born = jeision_born
        self.color = color

p1 = Myclass()
print(p1.a)

new_Animals = Animal ("emu", "86", "idk_narnia", "redish")
print(Animal.name)
print(Animal.age)
print(Animal.jeision_born)
print(Animal.color)