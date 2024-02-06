# 类

# Student为类名，()中的是继承的类，不知道继承什么类就选则object，因为所有类最终都会继承自他
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.age = 10
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        self.gender = False
        if self.score > 90:
            return 'A'
        elif self.score > 80:
            return 'B'
        elif self.score > 70:
            return 'C'
        else:
            return 'D'

a = Student('lihua', 120)
a.print_score()
print(a.age)

print(a)
print(Student)
