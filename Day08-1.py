import Yuzhe_pack as hyz
class Student(object):

    # 对象属性的定义（初始化）
    def __init__(self, name, age):
        self._name = name
        self._age = age
        # 函数的输入只是传入的参数，并不一定非要是对象属性的一部分
        # 可以视其为函数的自变量，对象的具体属性就是函数的因变量
        # 简单的说就是"传入参数还不够，还需要构造属性"

    # 对象行为的定义
    def study(self, course_name):
        print('%s正在学习%s' % (self._name, course_name))
        # 在行为构造的过程中，也要搞清楚使用的应该是"类的属性"，而不是"传入类的参数"

    def watch_movie(self):
        if self._age < 18:
            print('%s只能观看《熊出没》' % self._name)
        else:
            print('%s正在观看岛国爱情大电影' % self._name)


def main():
    stu1 = Student('weijia', 23)
    stu2 = Student('wangxueting', 17)
    stu1.study('希伯来语')
    stu2.study('高中课程')
    stu1.watch_movie()
    stu2.watch_movie()
    print(stu1._name)


if __name__ == '__main__':
    main()
    hyz.TIMESTAMP_POST()
