
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


def log(func):
    @functools.wraps(func)
    # 相当于dec.__name__ = func.__name__，并将这一句放在dec定义的后面
    def dec(*args, **kw):
        print(f"Calling {dec.__name__}(): ")
        return func(*args, **kw)
    return dec



def log(text):
    def dec1(func):
        def dec2(*args, **kw):
            print("the text is %s" %text)
            print(f"Calling {dec2.__name__}(): ")
            func(*args, **kw)
        return dec2
    return dec1

@log('excute')
def now():
    print("now")
now()
