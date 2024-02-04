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



# map
# map即为映射，将元素映射成另一种元素，类似于数学中的函数
def f(x):
    return x * x
r = map(f, [x for x in range(9)])
print(r)

n = 1
while(n < 5):
    print(next(r))
    n += 1


# reduce
# reduce(f, [x1, x2, x3]) = f(f(x1, x2), x3)
from functools import reduce

def f(a, b):
    return 10*a + b
print(reduce(f, [1,2,3,4, 5,6]))

def chartonum(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

def chartoint(s):
    return reduce(f, map(chartonum, s))

print(chartoint('12345'))



# 练习
# 1. 将首字母大写，其他小写
def normalize(name):
    s = name[1:].lower()
    return name[0].upper() + s
    pass

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 2. 求积
def prod(L):
    return reduce(lambda x, y: x * y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 3. 字符串转为浮点数
def strtofloat(s):
    def reverse(s):
        return s[::-1]
    index = s.find('.')
    pr, ed = s[:index], reverse(s[index + 1:])
    return reduce(lambda x, y: 10*x + y, map(int, pr)) + 0.1 * reduce(lambda x, y: 0.1 * x + y, map(int, ed))

print(strtofloat("123.456"))



# filter
# 筛子: 可以将列表中不满足要求的元素筛去
l = list(filter(lambda s: s and s.strip(), ['A', '', 'B', None, 'C', '  ']))
print(l)

# 构造一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        it = filter(lambda x: x % n > 0, it)
        yield n

index = 0
it = primes()
while index < 10:
    index += 1
    print(next(it))
