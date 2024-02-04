# 将函数作为返回值
def count():
    fs = []
    def g(i):
            def f():
                return i * i
            return f
    for i in range(1, 4):
        fs.append(g(i))
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


def createCounter():
    x = 0
    def counter():
        nonlocal x
        x += 1
        return x
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')




def logs(func):
    def wrapper(*args, **kw):
        print(f"Calling {func.__name__}(): ")
        return func(*args, **kw)
    wrapper.__name__ = func.__name__
    return wrapper

@logs
def now():
    print("hello, 2024")

print(now.__name__)


import time, functools

def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    return fn

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


def decorator(arg=None):
    def decorato(func):
        @functools.wraps(func)
        def dec(*args, **kw):
            print("begin call")
            func(*args, **kw)
            print("end call")
        return dec
    if callable(arg):
        return decorato(arg)
    else:
        return decorato

@decorator()
def funcs():
    print("use func")

funcs()
print(funcs.__name__)

