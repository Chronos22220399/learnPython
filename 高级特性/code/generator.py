
# L为一个生成器
L = (x * x for x in range(10) if x % 2 == 0)

# L可以通过next获取值，当对L使用了next后，L内部的指针将向后移一位，即L内部的指针会指向当前元素的下一个元素
# L也可以通过for循环迭代
# 因此，L本身是一个可迭代对象


# 自定义迭代器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

m = fib(9)

print(next(m))
print(next(m))

while True:
    try:
        print(next(m))
    except StopIteration as e:
        print("the Error is: ", e.value)
        break

# print(m)
# for n in m:
#     print(n, end='\t')


# 当使用next迭代完了fib中的元素后，继续使用next就会使得next函数抛出一个StopIterator的错误，我们可以使用return返回一个信息，该信息可以通过捕获StopIterator后通过其value获取
try:
    next(m)
except StopIteration as e:
    print('Generator return value: ', e.value)


print("----------------")
# 输出杨辉三角
def triangles():
    Ls = [1]
    while True:
        L = Ls[:]
        yield L
        n = len(Ls)
        Ls.append(1)
        i = n - 1
        while i > 0:
            Ls[i] = Ls[i] + Ls[i - 1]
            i -= 1
    pass

a = triangles()
print(a)
for n in range(10):
    print(next(a))

from collections.abc import Iterable

print(isinstance(a, Iterable))


print("-------------")
L = (pow(x, 3) for x in range(10))
print(L)
for n in L:
    print(n, end="\t")
print([L])


print("--------------")
def triangles():
    Ls = []
    def getTriangles(Ls):
        Len = len(Ls)
        Ls.append(1)
        n = Len - 1
        while n > 0:
            Ls[n] = Ls[n] + Ls[n - 1]
            n -= 1
        return Ls
    Ls = getTriangles(Ls)
    yield Ls

k = triangles()
for n in k:
    print(n)

L = [x if x % 2 == 0 else -x for x in range(10)]
print(L)