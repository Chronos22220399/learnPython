## 文件操作
### 打开文件
#### 使用`open`函数可打开文件，open的参数分别为（文件名、文件打开模式（和c语言的一样）、解析文件的字符编码、错误管理），返回值为对应的文件对象（文件描述符号）
示例：
```commandline
filename = "C:\\Users\\杨康\\Desktop\\TrafficManager.exe"
with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
    pass
except IOError as e:
    print("cannot open file", e)
```

### 读入文件
使用`read`函数可以读入文件，`read`函数中可以设置读入的大小


### 写文件
使用`write`函数可以写入文件

