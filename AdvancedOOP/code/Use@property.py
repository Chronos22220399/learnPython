class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError("the value is not integer")
        else:
            self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("the value is not integer")
        else:
            self._height = value

    @property
    def resolution(self):
        return self._height * self._width

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')