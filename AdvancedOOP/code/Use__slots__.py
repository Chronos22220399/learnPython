class Student(object):
     pass

s = Student()
s.name = "Ess Chronos"
print(s.name)

# 给实例绑定一个方法
def set_age(self, age):
     self.age = age

from types import MethodType
# 给s绑定方法set_age
s.set_age = MethodType(set_age, s)

s.set_age(19)
print(getattr(s, "age"))

# set_age方法只能给s使用，s2用不了
s2 = Student()

Student.set_age = MethodType(set_age, Student)

s2.set_age(100)
s3 = Student()
print("-----")
print(s.age)
print(s3.age)
print(Student.age)

# 限制类的属性
# 只有在元组内的属性名称才能在类中定义
class Animal(object):
     __slots__ = ("__name", "__age", "__gender")
     def __init__(self, name, age, gender):
          self.__name = name
          self.__age = age
          self.__gender = gender

class Cat(Animal):
     # __slots__ = ("__class")
     __slots__ = ("__class", "__name")
     def __init__(self, Class, name, age, gender):
          self.__class = Class
          self.__name = name
          super().__init__(name, age, gender)

     def get_name(self):
          return self.__name

ani = Animal("jack", 12, "female")
cat = Cat("cat", "cu", 11, "female")

# print(cat.get_name())
