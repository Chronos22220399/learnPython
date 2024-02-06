# __slots__ 限制类的属性
## 使用__slots__可以限制类使用哪些属性
### 语法：
```commandline
class SomeClass(object):
    __slots__ = ("Attr1", "Attr2")
```
这样SomeClass只能定义Attr1，Attr2属性（也可以不定义，或是选择性地定义）


## __slots__不会继承
###如果父类中定义了一些限制属性，则想要在子类中正常使用继承来的属性的话，必须在子类中重新限制（或是不限制）


## 绑定方法
### 在python中，我们可以为实例绑定方法，语法如下：
```commandline
from types import MethodType
class Student(object):
     pass
     
s = Student()

# 给实例绑定一个方法
def set_age(self, age):
     self.age = age
 
# 将set_age绑定到实例s上    
s.set_age = MethodType(set_age, s)
```
将set_age绑定到s上后，只有实例s能使用该方法，其他实例不能使用


### 为类绑定方法
```commandline
from types import MethodType

class Student(object):
     pass
     
# 给类绑定一个方法
def set_age(self, age):
     self.age = age
     
# 将set_age绑定到类Student上
Student.set_age = MethodType(set_age, Student)     
```
将set_age绑定到类Student上后，Student的实例（没有单独绑定这个函数的实例）都能访问这个方法，不够它们访问的是同一个方法
**在这样的方法中定义的变量将会成为类的变量，所有的实例（没单独绑定函数的）都将公用这一个方法和其中定义的变量
