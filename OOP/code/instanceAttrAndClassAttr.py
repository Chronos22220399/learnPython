class Student(object):
    name = 'Student'
    def __init__(self, name):
        self.__name = name

s = Student('Bob')
s.score = 90
print(Student.name)
print(s.name)


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1
        self.count = 1

a = Student("lihua")
print(a.count)
b = Student("liuming")
print(b.count)
