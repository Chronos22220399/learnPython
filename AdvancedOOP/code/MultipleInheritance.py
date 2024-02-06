class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class RunnableMixIn(object):
    def run(self):
        print("Running...")
        self.a = 19

class FlyableMixIn(object):
    def fly(self):
        print("Flying...")


class Dog(Mammal, RunnableMixIn):
    pass

class Cat(Mammal, RunnableMixIn):
    pass

class Bat(Mammal, FlyableMixIn):
    pass



class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__
print(Student("lihua"))
s = Student("s")
print(s)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

# 支持切片操作
    def __getitem__(self, n):
        a, b = 1, 1
        if isinstance(n, int):
            for x in range(n):
                a, b = b, a + b
            return a
        elif isinstance(n, slice):
            L = []
            start = n.start
            step = n.step
            if n.start == None:
                start = 0
            # 这里的切片操作的stop不能为None
            if n.step == None:
                step = 1

            for i in range(n.stop):
                if i >= start and i % step == 0:
                    L.append(a)
                a, b = b, a + b
            return L

a = Fib()
for n in a:
    print(n)
print('\n', a[8])
L = a[:9: 3]
print(L)


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' %(self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

c = Chain()
print(c.status.user.timeline.list)
