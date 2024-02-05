import functools
# 偏函数就是固定了函数的参数值的函数，相当于对原函数的特殊调用，很想数学中的偏函数（例如固定y的f(x, y)）
l = '12345'
a = int(l)
print(a)

int_8 = functools.partial(int, base=8)
print(int_8(l))

int_16 = functools.partial(int, base=16)
print(int_16(l))
