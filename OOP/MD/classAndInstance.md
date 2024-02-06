## 类和实例
### Python中的类是一种模板（不是泛型编程里的那个），而实例是类的实例化
### 类的定义
```commandline
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.age = 10

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        self.gender = 1
        if self.score > 90:
            return 'A'
        elif self.score > 80:
            return 'B'
        elif self.score > 70:
            return 'C'
        else:
            return 'D'
```

**注意：**
1. 类中不需要向C/C++、Swift等语言中那样定义变量（不需要按照它们的方式定义）, 要用时直接在方法中以赋值的方式定义即可，就像在类外一样
2. 类在定义时需要继承一个类，不知道继承哪个时继承object即可
3. 类的实例对象之间可能是不同的，因为可以在实例化后自定义属性
