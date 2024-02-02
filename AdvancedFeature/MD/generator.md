## 生成器（Generator）
### 普通定义列表生成器的对象
`L = (x * x for x in range(10))`

如上可获得一个列表生成器的对象

#### 调用方式
1. 使用next函数
   
    - next可以获取生成器对象
    - 使用了next函数后，next会指向当前对象的后一个对象（逻辑上的）
2. 使用for进行循环
   
   例如：
   ```python
   for n in L:
        print(n)
    ```

    这样可以输出L中的所有元素


### 自定义生成器

使用yield关键字即可自定义生成器，具体用法如下：
```
def fib(maxNum):
    n, a, b = 1, 0, 1
    while n <= maxNum:
        yield  b
        a, b = b, a + b
        n += 1
    return 'done'
```

在这段代码中定义了一个可以求斐波那契数列中的数字的生成器，当代码运行到yield处时便会将yield后面的值返回，并且代码会停止在此处

代码中的return行为生成器的终点，此时使用next会抛出一个StopIterator错误，此时这个错误的值就是return返回的值


**自定义生成器要和循环搭配使用**
