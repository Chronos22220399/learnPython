## 访问限制（AccessRestriction）
在Python的类中，若不想让内部的属性被外部使用以满足类的封闭性，可以在属性名称的的定义时加上“__”前缀，这样的变量属于私有变量
例如：
```commandline
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__age = 10
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        self.gender = False
        if self.__score > 90:
            return 'A'
        elif self.__score > 80:
            return 'B'
        elif self.__score > 70:
            return 'C'
        else:
            return 'D'

a = Student("lihua", 19)
```
此时无法查看属性__name,__age,__score只能在类内部使用

**总结：**
1. __Attribute：这种声明表示该Attribute是private的，不能被外部访问(但这也不是绝对的，因为解释器会把这类变量改写成_类名__Attribute的形式，但是不要这么做！)
2. __Attribute__：这种变量表明该Attribute是特殊变量，这种变量可以直接访问
3. _Attribute：这种变量是可以访问的，但是按照约定俗成的规定，这种变量应该视为私有变量（private），不能随便访问
4. 类中的普通函数f中定义了私有变量后，若在类的其他函数g中使用了该变量时，在调用该g前，应该先调用f，否则解释器会找不到该变量的SCF

<br>
# 题目：判断性别

```
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        if self.__gender not in ['male', 'female']
            raise ValueError("value Error：")
        else:
            return self.__gender
        
    def get_name(self):
        return self.__name

    def set_gender(self, gender='male'):
        if gender not in ['male', 'female']
            raise ValueError("value Error in func: set_gender")
        else:
            self.__gender = gender
```
