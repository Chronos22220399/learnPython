## 调试
### 调试方式
1. #### 使用print调试
用print将可能有错误的地方打印处理，这样可以锁定错误
<br>例如：
```commandline
# 使用print调试
def foo(s) :
    n = int(s)
    print(">>> n = %d" % n)
    return 10 / n

def main():
    foo('0')

main()
```
输出如下：
```commandline
>>> n = 0
Traceback (most recent call last):
  File "F:\learnPython\Error_DebugAndTest\code\Debug.py", line 11, in <module>
    main()
  File "F:\learnPython\Error_DebugAndTest\code\Debug.py", line 9, in main
    foo('0')
  File "F:\learnPython\Error_DebugAndTest\code\Debug.py", line 6, in foo
    return 10 / n
           ~~~^~~
ZeroDivisionError: division by zero
```
上面输出了0，这就是错误的原因，因为除数不能为0 <br>
**劣势：在查找出错误后删除print会比较麻烦**

<br>


2. #### 使用断言（assert）
断言语法如下：`assert condition, 'message'
当condition不满足时，就会输出message
例如：
```commandline
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
```
输出结果如下：
```commandline
Traceback (most recent call last):
  File "F:\learnPython\Error_DebugAndTest\code\Debug.py", line 23, in <module>
    main()
  File "F:\learnPython\Error_DebugAndTest\code\Debug.py", line 21, in main
    foo('0')
  File "F:\learnPython\Error_DebugAndTest\code\Debug.py", line 17, in foo
    assert n != 0, 'n is zero!'
AssertionError: n is zero!
```
**优势：如果满足condition后面的语句就不会发送，后续不用删除，而且后续可以在终端使用 `python -O fileName` (O时大写的o)来关闭assert**

<br>

3. 使用logging
logging不会抛出错误，而且能把错误传输到文件供后续观看
```commandline
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
```
 **level有debug、info、warning、error这几个级别，使用第i个的等级，第1 --- i-1个等级会失效，后面的都会生效**
 
<br>

4. 使用IDE的调试器


## 总结：logging最好用
