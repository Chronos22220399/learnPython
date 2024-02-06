## 枚举类
### 定义
1. #### 直接将其定义为枚举类型（枚举实际上也是一个类）
语法：Enum('枚举名称',*args(枚举的内容物))
例子：
```commandline
from enum import Enum

# 定义
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 使用
jan = Month.Jan
print(jan)     # 输出：Month.Jan
print(jan.value) # 输出：1 默认从1开始

# 遍历
for name in Month.__members__.items():
    print(name)
for name, member in Month.__members__.items():
    print(name, member)
```

2. #### 定义一个继承枚举类的类
```commandline
from enum import Enum, unique
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    The = 4
    Fri = 5
    Sat = 6
    
# 用法和上面的相同
# @unique用于检查保证没有重复值
```
