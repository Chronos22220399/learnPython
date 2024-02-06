class Animal(object):
    def Speak(self):
        self.__loud = "www"
        print("the animal is speaking")

    def eat(self):
        print(self.__loud)
        print("the animal is eatting")

class Cat(Animal):
    def Speak(self):
        self.__loud = "miao"
        print("the cat is speaking")

    def eat(self):
        print(self.__loud)
        print("the cat is eatting")
    pass

class Dog(Animal):

    def Speak(self):
        self.__loud = "wang wang wang"
        print("the dog is speaking")

    def eat(self):
        print("the dog is eatting")

cat = Cat()
dog = Dog()

# 多态
def speak(animal=Cat()):
    animal.Speak()

speak(cat)
speak(dog)

import types

print(type(cat))
print(type(dog))
print(type(Cat))

# 使用isinstance不仅可以看出实例和类的关系，还能看出和父类的关系
print(isinstance(cat, Animal))

print(hasattr(dog, "_Dog__loud"))
print(getattr(dog, "_Dog__loud"))

a = getattr(dog, "s")

