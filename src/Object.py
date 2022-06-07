class Object():
    def __init__(self, age):
        self.age = age
    pass

human = Object(5)
human.age = 10
monkey = Object(6)
print(human)
print(human.age)
print(monkey.age)