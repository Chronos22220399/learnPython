## 自定义类
### 在类中可以定义一些函数实现类的自定义，如使用__str__改变类的说明（使用print直接输出类时），使用__call__可以直接把类当作函数调用等

1. #### \_\_init__
使用__init__可以创建自己需要的属性，很常见，这里就不多说明

<br>

2. #### \_\_str__
使用__str__可以改变对类直接使用print函数时的输出
例如：
```commandline
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
        
print(Student("lihua"))

# 输出：Student object (name: lihua)
```

<br>

3. #### \_\_repr__
__str__改变的是print显示的内容，而__repr__改变的是终端输出的结果，前者针对客户端，后者针对开发者
例如：
```commandline
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__
    
 # 或者
 
 class Student(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Student object (name: %s)' % self.name
```
前者更方便也更常用，因为不许要额外做定义了，而后者还要做对__str__的定义（当然，也可以不做）

<br>

4. #### \_\_iter__和__next__
__iter__可以将对象变成Iterable，而__next__可以让对象成为Iterator

这两个方法最主要的作用就是让对象可迭代，以被for使用，因此，要被for迭代的话，__iter__是一定要有的，而在__iter__返回一个可迭代对象的情况下，__next__不需要写，因为返回的对象中内置有__next__方法
例如：
```commandline
# 不写__next__方法
class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        # 返回一个迭代器，这里简单地使用 iter() 函数
        return iter(self.data)

# 创建一个可迭代对象
my_iterable = MyIterable([1, 2, 3])

# 使用 for 循环迭代可迭代对象
for item in my_iterable:
    print(item)

# 写__next__方法
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
```

在第一端代码中，返回的iter(self.data)是可用for迭代的，所以不用写__next__方法了，而第二段代码需要写，因为__iter__方法返回的是对象本身，只靠这个无法获得下一个值，会无法迭代
<br>


5. #### \_\_getitem__
__getitem__能让对象实现下标操作和切片操作
例如：
```commandline
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
        
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
```

<br>

6. #### \_\_getattr__
__getattr__方法可以获取类未定义的属性，这是因为当类中不存在的属性被访问时，解释器会以属性名为参数直接访问__getattr__方法，我们可以自定义__getattr__方法以应对访问到不存在的参数时的情况，这样可以防止解释器报错而停止工作
例如：
```commandline
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
```
这是一段链式调用，以显示信息
