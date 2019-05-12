# %%
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# example of multiple inheritance avoid this in real app


class Mammal(Animal):
    def walk(self):
        print("walk")


class Dog(Mammal, Animal):
    def woof(self):
        pass


class Fish(Animal):
    def __init__(self, weigth):
        super().__init__()
        self.weigth = weigth

    def swim(self):
        print("swim")


fish = Fish(100)
fish.eat()
fish.swim()
print(fish.age)
print(fish.weigth)
print(isinstance(fish, Fish))
print(isinstance(fish, Animal))
