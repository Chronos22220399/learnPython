class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__age = 10
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        self.gender = False
        if self.__score > 90:
            return 'A'
        elif self.__score > 80:
            return 'B'
        elif self.__score > 70:
            return 'C'
        else:
            return 'D'

a = Student("lihua", 19)


# 练习
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        if self.__gender not in ['male', 'female']:
            raise ValueError("value Error：")
        else:
            return self.__gender

    def get_name(self):
        return self.__name

    def set_gender(self, gender='male'):
        if gender not in ['male', 'female']:
            raise ValueError("value Error in func: set_gender")
        else:
            self.__gender = gender

