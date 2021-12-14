import random

def roll(dices):
    dices = dices.upper()
    times, choice = [int(num) for num in dices.split('D')]
    result = [random.randint(1,choice) for i in range(times)]
    return result

class Player:
    def __init__(self, name, abi_dict):
        self.name = name
        self.ability = abi_dict
        # {
        #     'INT': abi_data[0],
        #     'SPT': abi_data[1],
        #     'MAG': abi_data[2],
        #     'STR': abi_data[3],
        #     'DEX': abi_data[4],
        #     'LIF': abi_data[5],
        #     'CHI': abi_data[6],
        #     'STM': abi_data[7],
        #     'LUK': abi_data[8]
        # }
        self.elem_status = {
            'is_fire': False,
            'is_aqua': False,
            'is_rock': False,
            'is_wood': False,
            'is_light': True,
            'is_dark': False
        }

        self.hp = 100 + 10*self.ability['LIF']
        self.bp = 100 + 10*self.ability['CHI']
        self.ap = 10 + 2*self.ability['STM']

    def hit(self, to_whom, card):
        damage = card.checkout()
        to_whom.bp -= damage['value']
        if to_whom.bp < 0:
            to_whom.hp += to_whom.bp
            to_whom.bp = 0
        print('>>> %s hits %s with [%s] damage %d!' % (damage['from_whom'].name, to_whom.name, damage['type'],damage['value']))


    def __str__(self):
        status = '''
    -------------------
    > NAME: %s
    * Health: %d
    * Barrier: %d
    * Stamina: %d
    -------------------
        ''' % (self.name, self.hp, self.bp, self.ap)
        return status

def check_condition(list):
    for requirement in list:
        if not requirement:
            return False
    return True




class Card:
    def __init__(self, holder):
        self.card_name = '灵魂波动'
        self.card_type = '灵魂技艺'
        self.card_text = '使灵魂和空间共振产生波动，是最基本的灵魂技艺。很多人不经过学习也能掌握这种魔法。'

        self.holder = holder

        self.is_ACT = True
        self.cost = 3

        self.basic = 'MAG'
        self.basic_scale = 0.8
        self.extra = '3D4'
        self.extra_scale = 1

        self.damage_type = 'magic'
        self.elem_type = None
        self.is_remote = True

        self.is_avaliable = check_condition(
            [self.holder.elem_status['is_light']==True,
             self.holder.ability['MAG']>=3]
        )

    def checkout(self):
        basic = self.holder.ability[self.basic] * self.basic_scale
        extra = sum(roll(self.extra)) * self.basic_scale
        damage = {
            'value': int(basic+extra),
            'type': self.damage_type,
            'from_whom': self.holder
        }
        return damage

ability = {}
ability['INT'] = 1
ability['SPT'] = 1
ability['MAG'] = 5
ability['STR'] = 2
ability['DEX'] = 1
ability['LIF'] = 1
ability['CHI'] = 1
ability['STM'] = 1
ability['LUK'] = 0


player1 = Player('Coconuts',ability)
player1.light = True
player2 = Player('dnd',ability)

card1 = Card(holder=player1)

player1.hit(player2, card1)
