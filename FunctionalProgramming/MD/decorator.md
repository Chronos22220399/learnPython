## 装饰器（decorator）
使用@加对应的装饰函数进行装饰
例如：
```commandline
import functools

def log(func):
    @functools.wraps(func)
    # 相当于dec.__name__ = func.__name__，并将这一句放在dec定义的后面
    def dec(*args, **kw):
        print(f"Calling {dec.__name__}(): ")
        return func(*args, **kw)
    return dec
    
@log
def now():
    print("now")
@log用在定义时相当于：
# now = log(now)
```

### 传入参数的装饰器
在装饰器中传入参数使用
```commandline
import functools

def log(text):
    def dec1(func):
        @functools.wraps(func)
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
```
使用这种写法就相当于 `now = log('excute')(now)`
调用`log('excute')`时返回了函数dec1，此时相当于`now = dec1(func)`


### 既可以传入参数也可以不串的修饰器
```commandline
import functools

def decorator(arg=None):
    def dec(func):
        @functools.wraps(func)
        def dec1(*args, **kw):
            print("begin call")
            func(*args, **kw)
            print("begin call")
        return dec1
    
    if callable(arg):
        return dec(arg)
    else:
        return dec        
```
