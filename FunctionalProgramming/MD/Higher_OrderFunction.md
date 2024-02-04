## 高阶函数
1. ### 函数本身能够赋值给对象
    猜测原因是因为python中的变量本质是应用的缘故
2. ### 函数本身就是一个对象
    `abs = 10`这段代码是成立的
3. ### 函数可以作为参数使用
    ```
   def add_abs(x, y, fabs):
    return fabs(x) + fabs(y)
   ```
   外层的add_abs函数就是所谓的高阶函数


## map
map就是一种类似于数学中的函数的映射，其用法为
`map(func, Iterable_Object)`
，它会将Iterable_Object按照func映射成一个迭代器（Iterator）

例如：

```commandline
f = lambda x: x if x % 2 == 0 else 0
print(list(map(f, [x for x in range(10)])))
# 输出：[0, 0, 2, 0, 4, 0, 6, 0, 8, 0]
```


## reduce
reduce是对可迭代对象（Iterable）中的元素按顺序作为函数的参数运算，函数的结果会作为下一层函数与列表中下一个元素的参数使用，简单来说就是：

`reduce(sum, [1,2,3,4,5]) == sum(sum(sum(sum(1, 2), 3), 4), 5)`

使用实例：
```commandline
# 2. 求积
def prod(L):
    return reduce(lambda x, y: x * y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
```

```commandline
# 3. 字符串转为浮点数
def strtofloat(s):
    def reverse(s):
        return s[::-1]
    index = s.find('.')
    pr, ed = s[:index], reverse(s[index + 1:])
    return reduce(lambda x, y: 10*x + y, map(int, pr)) + 0.1 * reduce(lambda x, y: 0.1 * x + y, map(int, ed))

print(strtofloat("123.456"))
```



## filter
如起名，filter像筛子一样会筛掉可迭代对象（Iterable）中不符合条件的元素，其返回值也是一个Iterator类型的引用

**用法：**
```
l = filter(lambda x: x % 2 == 0, [1,2,3,4,5])
print(list(l))
# 结果为[2,4]
```

使用实例：
```commandline
# 使用埃氏筛法获取质数
def _odd_iter():
    n = 1
    while n < 1000:
        n = n + 2
        yield n

def primes():
    # yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        it = filter(lambda x, n = n: x % n > 0, it)
        yield n

index = 0
it = primes()
while index < 20:
    index += 1
    print(next(it))
```


## sorted
sorted用于对可迭代对象进行排序，其内部有三个参数，第一个必选，后两个可选
```commandline
sorted(Iterable, key=function, reverse)
# function为函数名称，这里是对函数的引用，reverse是一个布尔值，reverse=True时表示选择反转
```

实例：
```commandline
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# 输出：
# ['Credit', 'Zoo', 'about', 'bob']
# ['about', 'bob', 'Credit', 'Zoo']
# ['Zoo', 'Credit', 'bob', 'about']
```
