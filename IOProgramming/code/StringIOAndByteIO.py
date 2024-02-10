from io import StringIO, BytesIO

with StringIO("Hello?\nHi!\nGoodbye!") as Str:
    while True:
        s = Str.readline()
        if s == '':
            break
        print(s.strip())
    st = input("input your content: ")

    index = Str.tell()

    Str.write(st)
    # 打印输入部分的内容]
    Str.seek(index, 0)
    print("输入部分的内容:", Str.read())
