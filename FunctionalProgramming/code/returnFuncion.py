# 将函数作为返回值
def count():
    fs = []
    def g(i):
            def f():
                return i * i
            return f
    for i in range(1, 4):
        fs.append(g(i))
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


def createCounter():
    x = 0
    def counter():
        nonlocal x
        x += 1
        return x
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
