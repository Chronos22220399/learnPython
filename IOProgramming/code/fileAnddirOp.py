import logging
import os
import ctypes
# #
# # print(os.name)
# #
# # print(os.environ.get('COMPUTERNAME'))
# #
# # print(os.environ.get('x', 'default'))
# #
# # print(os.path.abspath('.'))
# #
# # print(os.path.join(os.path.abspath('.'), 'testdir'))
# #
# #
# # try:
# #     os.mkdir(os.path.join(os.path.abspath(''), 'testdir'))
# # except FileExistsError as e:
# #     print('cannot create file, because', e)
# #
# # # try:
# # #     os.rmdir(os.path.join(os.path.abspath(''), 'testdir'))
# # # except FileNotFoundError as e:
# # #     print('cannot del file, because', e)
# #
# #
# # os.chdir('F:\\learnPython\\IOProgramming\\code')
# # print(os.getcwd())
#
# print("--------------")
#
# # 文件的总块数（以4k为单位）
# # 文件类型和权限   类型：os.path.splitext(path)   权限：os.access(path, mode) (mode: os.F_OK\os.R_OK\os.W_OK\os.X_OK)
# # 链接数
# # 文件大小或目录的大小
# # 文件的最后修改时间
# # 文件或目录的名称
# def dir_l(name):
#     total_block = 0
#     now_path = os.path.abspath('.')
#     File = dict()
#
#     # 获取文件路径
#     def get_abspath(name):
#         f_path = os.path.join(now_path, name)
#         return f_path
#
#     # 获取大小
#     def getSize(name):
#         nonlocal total_block
#         size = os.path.getsize(get_abspath(name))
#         total_block += int(size)
#         return size
#
#     # 获取文件类型以及权限、大小
#     def get_typeAndAccess(name):
#         path = get_abspath(name)
#         # 获取文件后缀
#         f = os.path.splitext(path)
#         # 获取文件名
#         f_name = os.path.split(f[0])
#         if str(f_name) not in File:
#             File[str(f_name[1])] = []
#         File[str(f_name[1])].append(f[1])
#
#         access = 'Find'
#         if os.access(path, os.F_OK):
#             if os.access(path, os.R_OK):
#                 access = 'Read'
#                 if os.access(path, os.W_OK):
#                     access = 'Write'
#                     if os.access(path, os.X_OK):
#                         access = 'Both'
#
#         File[str(f_name[1])].append(access)
#         File[str(f_name[1])].append(getSize(name))
#
#     for fileOrDir in os.listdir():
#         get_typeAndAccess(fileOrDir)
#
#         if os.path.isfile(os.path.join(now_path, fileOrDir)):
#             pass
#
#     # 获取文件所有者   暂时不写
#     def get_file_owner(file_path):
#         try:
#             pass
#         except Exception as e:
#             logging.exception(e)
#             pass
#
#     owner_name = get_file_owner(name)
#     print(File)
#     # print(owner_name)
#
# dir_l('F:\\learnPython\\IOProgramming\\code')

import json

# json.dumps(obj) 将对象序列化为Json内容的字符串
# json.dump(obj, f) 将对象序列化为Json内容的字符串后写入feel-like Object中
# json.loads() 将Json字符串反序列化
# json.load() 从feel-like Object中读取字符串并反序列化
# d = {'name': 'Bob', 'age': 20, 'score': 88}
#
# d['gender'] = 'male'
# with open(r'dump_.txt', 'w') as f:
#     json.dump(d, f)
#
# with open(r'dump_.txt', 'rb') as f:
#     content = json.load(f)
#     print(content)

class Student(object):
    def __init__(self, name, age, score):
        self.__name__ = name
        self.__age__ = age
        self.__score__ = score

    @classmethod
    def Student_init(cls, **kw):
        name = kw['name']
        age = kw['age']
        score = kw['score']
        return cls(name, age, score)

s = Student('iris', 20, 88)
p = Student('Ess', 20, 100)

def Obj2Json(std):
    return {
        'name' : std.__name__,
        'age' : std.__age__,
        'score' : std.__score__
    }


with open(r'dump_.txt', 'w') as f:
    json.dump(s, f, default=Obj2Json)
    f.write('\n')
    json.dump(p, f, default=lambda obj:obj.__dict__)
    content = json.dumps(p, default=Obj2Json)
    print(content)

with open(r'dump_.txt', 'r') as f:
    lines = f.readlines()
for line in lines:
    obj = line.strip('\n')
    json_obj = json.loads(obj)
    print(json_obj)
