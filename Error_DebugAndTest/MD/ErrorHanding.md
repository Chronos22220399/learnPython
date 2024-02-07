## 错误处理（Error Handing）
### 错误处理的主要方式如下：
1. #### try
```commandline
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
```

2. #### 调用栈
```commandline
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main()
```
如上代码报出的错误：
```commandline
Traceback (most recent call last):
  File "F:\learnPython\Error_DebugAndTest\code\Debug.py", line 10, in <module>
    main()
  File "F:\learnPython\Error_DebugAndTest\code\Debug.py", line 8, in main
    bar('0')
  File "F:\learnPython\Error_DebugAndTest\code\Debug.py", line 5, in bar
    return foo(s) * 2
           ^^^^^^
  File "F:\learnPython\Error_DebugAndTest\code\Debug.py", line 2, in foo
    return 10 / int(s)
           ~~~^~~~~~~~
ZeroDivisionError: division by zero
```
在处理错误时从栈顶一步步往下看就能看明白哪里出错了

3. #### logging
使用logging记录错误，这种方式在不会使程序停止运行的同时还能清晰地通过查看错误记录查找错误，而且logging可以将记录打印在文件中，便于后续查看

4. #### 捕获错误后再抛出，交给上层去处理
```commandline
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
```

### 抛出错误
raise + 错误即可抛出错误
例如： `raise ValueError("message")`

### 自定义错误
错误是一种类，我们可以通过继承错误类来自定义错误
例如：
```commandline
class FooError(ValueError):
    pass
```
这样定义出来的错误类可以像python自带的错误一样使用
