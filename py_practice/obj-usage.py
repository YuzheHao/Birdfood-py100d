import Yuzhe_pack as hyz

class man(object):
    # 限定对象只能绑定这些属性，要是不限定的话，在外部也可以随便给类添加新属性
    __slots__ = ('_name', '_age', '_gender','_call')

    def __init__(self,name,age,gender):
        self._name = name
        self._age = age
        self._gender = gender
        if self._gender == 'male':
            self._call = 'he'
        elif self._gender == 'female':
            self._call = 'she'
        else:
            self._call = 'it'

    ''' 
    [使用getter和setter的原因]：
    其实在外部也可用通过[entity._name = 'xxx']这样的方法实现对类属性
    的访问和修改；但是[_name]这样带下划线的类内属性变量为应当避免在外部
    出现，所以才使用了getter和setter方法，来建立带下划线的属性和不带下
    划线的变量之间的映射关系。
    '''
    # 访问器 - getter方法
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @property
    def gender(self):
        return self._gender
    # 修改器 - setter方法
    @name.setter
    def name(self, name):
        self._name = name
    @age.setter
    def age(self, age):
        self._age = age
    @gender.setter
    def gender(self, gender):
        self._gender = gender

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

    def __str__(self):
        return '%s is %s, and %s is %s-years-old.' \
                % (str(self._name),str(self._gender),str(self._call),str(self._age))


def main():
    man1 = man('Levine',22,'male')
    print(man1)
    print(man1.name)
    print(man1.age)
    print(man1.gender)
    print(man1._call)
    # 如果不[__slots__]的话，这里也可以随便加新属性进去
    # man1._marriage = 'True'
    # print(man1._marriage)

if __name__ == '__main__':
    main()
