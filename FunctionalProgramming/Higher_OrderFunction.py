# 1. 函数本身能够赋值给变量
f = abs
print(f == abs)


# 2. 函数名也是变量
# 函数名其实就是指向函数的变量
# abs = 10 这是成立的


# 3. 函数可以作为参数
def add_abs(x, y, fabs):
    return fabs(x) + fabs(y)

print(add_abs(-12, 12, abs))

