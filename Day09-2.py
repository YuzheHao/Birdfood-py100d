import Yuzhe_pack as hyz
import random

class Card(object):

    __slots__ = ['_suite', '_face']

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    def __str__(self):
        if self._face == 1:
            str_face = 'A'
        elif self._face == 11:
            str_face = 'J'
        elif self._face == 12:
            str_face = 'Q'
        elif self._face == 13:
            str_face = 'K'
        else:
            str_face = str(self._face)
        return '%s%s' % (self._suite,str_face)

    def __repr__(self):
        return self.__str__() # 将对象的str表达式扩展至全局


class Poker(object):

    def __init__(self):
        self._cards = [Card(suite, face)
                        for suite in '♠♥♣♦'
                        for face in range(1, 14)] # 按规则循环构建list的一种方法
        self._top = 0 # 当前牌堆顶部的位置索引

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        self._top = 0
        random.shuffle(self._cards)

    def next(self):
        if self._top == len(self._cards):
            print("牌已发完！！")
        else:
            self._top += 1
            return self._cards[self._top-1]


class Player(object):

    def __init__(self,name):
        self._name = name
        self._hand = []
        self._ace_flag = 0
        self._sum = 0

    @property
    def hand(self):
        return self._hand

    def get(self,newcard):
        self._hand.append(newcard)
        if newcard.face == 1:
            self._ace_flag = 1
        self._sum = 0
        for cards in self._hand:
            if cards.face >10:
                self._sum += 10
            else:
                self._sum += cards.face
        if self._ace_flag == 1:
            if (self._sum-1<12):
                self._sum += 9


def main():
    p1 = Poker()
    p1.shuffle()
    print(p1.cards)
    me = Player('You')
    banker =Player('Banker')

    banker.get(p1.next())
    me.get(p1.next())
    for i in range(5):
        if me._sum > 21:
            print('You are BOOMED!')
        if banker._sum >21:
            print('Banker is BOOMED')
        print('目前庄家的手牌为：', banker._hand)
        print('目前你的手牌为：', me._hand)
        ans = input("您是否继续要牌?(Y/N) ");
        if ans == 'Y':
            me.get(p1.next())
        if (21-banker._sum) > 3:
            banker.get(p1.next())
        print('')



    if (21-banker._sum)<=(21-me._sum):
        print('Banker WINS!')
    else:
        print('You WINS!')


        # print('目前的点数和为：', me._sum, '\n')


if __name__ == '__main__':
    main()
