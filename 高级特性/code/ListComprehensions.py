# 普通的列表生成器
L = [x for x in range(19)]
print(L)


# 高级一点的
# 对x的更改直接写在for的前面即可
L = [x * x for x in range(10)]
print(L)


# 删选
# if 后的语句作为列表生成器的筛子
L = [x for x in range(10) if x % 2 == 0]
print(L)

# 如果使用if else语句的话，if else要放在for的前面，此时if else起分支作用
# 若if语句成立则生成if前面的内容，否则生成else后面的内容
L = [x if x % 2 == 0 else -x for x in range(10)]
print(L)

# 双层循环
M = [m + n for m in 'ABC' for n in '123']
print(M)


import os           # 导入os模块
print([d for d in os.listdir('.')])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)