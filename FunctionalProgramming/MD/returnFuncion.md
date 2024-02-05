## 将函数作为返回值
就是将函数作为返回值，例如：
```commandline
def func1():
    def func2():
        pass
    return func2
```
<br>

### 需要注意的是，当返回的函数中有对外部变量的引用时，该返回的函数称为闭包，该值则以引用的形式出现
例如：
```commandline
def count():
    fs = []
    def f():
        return i * i
    for i in range(1, 4):
        fs.append(f)
        
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

# 输出: 9 9 9
```
原因：

f1, f2, f3接收到的是闭包，该闭包引用了外部变量i的值，当闭包传出后，i的值为3，所以结果是9 9 9 



### 在函数中直接对外部变量进行赋值操作时会将该外部变量当成内部变量，这个内部变量和外部变量没有关系，只是名字相同
在这种情况下，如下情况会报错：
```commandline
def func1():
    x = 1
    def func2():
        x = x + 1
    func2()
    
func1()
```
因为x此时是内部变量，而x + 1部分则相当于将一个没有初始化的变量加到x上，所以会报错
正确的做法是在x = x + 1前面加上`nonlocal x`，声明x不是内部（本地）变量，而是外部变量
```commandline
def func1():
    x = 1
    def func2():
        nonlocal x
        x = x + 1
    func2()
func1()

```
