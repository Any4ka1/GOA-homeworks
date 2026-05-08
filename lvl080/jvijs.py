class dog:
    def __init__(self, name = "bernard", age = 5):
        self.name = name
        self.age = age
    def __str__(self):
        f"name: {self.name}, age: {self.age} "
    def griting(self):
        return "charlie_kirk"
new_g = dog()
print(new_g)
print(new_g.griting())

class Cat:
    def __init__(self, name, age):
        dog.__init__(self, name = "otori", age = 8970)
        self.name = name
        self.age = age

    def __str__(self):
        return f"name: {self.name}, age: {self.age} "