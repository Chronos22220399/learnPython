## 迭代器（Iterator）

### 判断是否是可迭代对象（Iterable）
可迭代对象都可以通过for循环遍历使用
使用自带的isinstance函数和在collections.abc中的Iterable关键字即可判断是否是可迭代对象
```
from collections.abc import Iterable

def col():
    n = 0
    while n < 19:
        yield n
        n += 2

n = col()
print(isinstance(n, Iterable))
# 输出True

print(isinstance("abc", Iterable))
#输出True
```
**所有的集合对象以及生成器和自定义生成器的对象均为可迭代对象**


### 迭代器（Iterator）
生成器（包括自定义）都是Iterator，但是list、dict、str虽然手术Iterable对象，但都不是Iterator，不过它们都可以通过iter()函数转化成Iterator
例如：
```
print(isinstance(iter([]), Iterator))
# 输出 True

print(isinstance(iter('abc'), Iterator))
# 输出 True
```


### 小结
1. 可使用isinstance函数判断对象是否为Iterator
2. 可使用Iter函数将Iterable对象转化为Iterator
3. Iterator对象是一个数据流，可能无法推测出全部，例如自然数集，它是一个惰性序列，而普通的集合类型对象是一个集合，是可推断出全部的，例如[1,2,3,4,5]