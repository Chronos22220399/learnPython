
# 保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self, name, column_type):
        self._name = name
        self._column_type = column_type

    def __str__(self):
        return '<%s : %s>' % (self.__class__.__name__, self._name)


# 在Field的基础上定义其他字段类型
# 字符串字段
class StringField(Field):
    def __init__(self, name):
        super().__init__(name, 'varchar(100)')


# 整形字段
class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, 'bigint')


# 编写元类
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        print('Found Model: %s' % name)

        mappings = dict()

        # 建立映射关系
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings
        attrs['__table__'] = name

        return type.__new__(cls, name, bases, attrs)


# 编写基类Model
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v._name)
            params.append('?')
            args.append(getattr(self, k, None))

        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ', '.join(fields), ', '.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
    pass


# 因为继承了dict，所以u本身保存了这些信息，而User类里的属性只是用来创建映射的
u = User(ip='12345', name='Ess Chronos', password='my-pwd', email='Ess.ink')

u.save()
print(u)
