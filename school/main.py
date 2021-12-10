import random

def roll(dices):
    dices = dices.upper()
    times, choice = [int(num) for num in dices.split('D')]
    result = [random.randint(1,choice) for i in range(times)]
    return result

def hurt(player, damage):
    player.bp -= damage
    if player.bp < 0:
        player.hp += player.bp
        player.bp = 0
    print('>>> %s got damege %d!' % (player.name, damage))
    print(player)

def ability_gen(data):
    ability = {}
    ability['INT'] = data[0]
    ability['SPT'] = data[1]
    ability['MAG'] = data[2]
    ability['STR'] = data[3]
    ability['DEX'] = data[4]
    ability['LIF'] = data[5]
    ability['CHI'] = data[6]
    ability['STM'] = data[7]
    ability['LUK'] = data[8]
    return ability

class Player:
    def __init__(self, name, ability):
        self.INT = ability['INT']
        self.SPT = ability['SPT']
        self.MAG = ability['MAG']
        self.STR = ability['STR']
        self.DEX = ability['DEX']
        self.LIF = ability['LIF']
        self.CHI = ability['CHI']
        self.STM = ability['STM']
        self.LUK = ability['LUK']

        self.fire = False
        self.aqua = False
        self.rock = False
        self.wood = False
        self.light = False
        self.dark = False

        self.name = name
        self.hp = 100 + 10*self.LIF
        self.bp = 100 + 10*self.CHI
        self.ap = 10 + 2*self.STM

    def hit(self, player, damage, type):
        player.bp -= damage
        if player.bp < 0:
            player.hp += player.bp
            player.bp = 0
        print('>>> %s hits %s with [%s] damage %d!' % (self.name, player.name, type, damage))


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


name = 'Coconuts'
ability = ability_gen([1,1,1,1,1,1,1,1,1])
player1 = Player('Coconuts',ability)
player2 = Player('dnd',ability)
