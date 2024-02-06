# 继承和多态(inheritance and polymorphism)
## 继承
### 继承是从其他类中继承相应的方法，继承来的方法可以直接使用，也可以重新实现来覆盖掉原来的方法
#### 继承语法
```commandline
class myClass(object):
    pass
```
这里的object就是继承的类，名为父类，而myClass则是子类，myClass中会有object中的所有方法

**需要注意的是：**
重写继承来的方法时，如果其中用到了在父类中定义的私有属性（private Attribute）时，需要重写定义该私有属性的方法，否则会报错


## 多态
### 多态是一种函数根据参数的不同实现不同的结果
多态是基于类实现的，在函数中使用类中的方法，则在使用该函数时，传入的参数只要有该方法即可产生多态，**该函数只能由拥有这种方法的类的对象调用**

实例：
```commandline
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
        print(self.__loud)
        print("the dog is eatting")

cat = Cat()
dog = Dog()

# 多态
def speak(animal=Cat()):
    animal.Speak()

speak(cat)
speak(dog)

# 输出
the cat is speaking
the dog is speaking
```
