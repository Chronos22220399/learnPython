# 获取对象信息
## 查看对象类型
使用type和isinstance可以查看对象类型，type只能看到当前类的信息，而isinstance可以对当前类及其父类进行判断，所以优先使用isinstance判断
```commandline
# 几个类的定义在InheritanceAndPolymorphism.py中，这里就不写了
print(type(cat))
print(type(dog))
print(type(Cat))

print(type(cat) == Animal)
# 输出：False
print(type(cat) == Cat)
# 输出：True

print(isinstance(cat, Animal))
print(isinstance(cat, Cat))
# 分别输出：True、True
```

### 查看对象有无某一属性
`hasattr(Object, 'Attribute_name')` (这里的Object单纯指对象)
### 获取对象某一属性
`getattr(Object, 'Attribute_name')`

若对象的该属性不存在则会抛出AttributeError错误
### 设置对象某一属性
`setattr(Object, 'Attribute_name', Attribute_value)`

若对象的该属性不存在则会创建该属性
