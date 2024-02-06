from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month)

for name, member in Month.__members__.items():
    print(name, "=>", member, ', ', member.value)


print(Month['Jan'].value)

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    The = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(Weekday['Mon'])


for name in Month.__members__.items():
    print(name)


# 练习
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender



Hee = (type('Hee', (object,),dict()))
print(type(Hee))
