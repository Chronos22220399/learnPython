#!/user/bin/env python3
# -*-coding: utf-8 -*-

# 第一二行为标准注释，第一行注释让这个文件可以在Unix/Linux/Mac上使用，第二行注释表示这个py文件本身使用utf-8编码

# 文档注释
'a test module'
# 作者
__author__ = "Ess Chronos"

import sys

def test():
    args = sys.argv
    print(args[0])
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

print(sys.path)
