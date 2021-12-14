import os
import numpy as np
import json
import pandas as pd


def read_card(list):
    box = {}
    box['card_type'] = list[0]
    box['card_name'] = list[1]
    box['act_type'] = list[2]
    box['card_text'] = '以后再写！'
    box['act_text'] = list[7]

    # 3基础伤害， 4附加伤害， 5伤害削减
    if type(list[3]) != float and type(list[4]) != float:
        if list[4][0] == '-':
            list[4] = ' - ' + list[4][1:]
        else:
            list[4] = ' + ' + list[4]
    if type(list[3]) == float: damage_base = ''
    else: damage_base = list[3]
    if type(list[4]) == float: damage_extra = ''
    else: damage_extra = list[4]
    if type(list[5]) == float: damage_cut = ''
    else: damage_cut = list[5]
    box['act_damage'] = '%s%s%s' % (damage_base, damage_extra, damage_cut)

    # 6体力消耗
    if list[6][0] == '(':
        free, fee = [int(x) for x in list[6][1:].split(')')]
        box['act_cost'] = '✧'*free + '✦'*fee
    else:
        box['act_cost'] = '✦'*int(list[6])

    # 8使用条件
    if type(list[8]) != float:
        box['act_condition'] = list[8]
    else:
        box['act_condition'] = None


    return box



file_path = "/Users/Yuzhe/Desktop/cards.csv"
df = pd.read_csv(file_path, sep = ',', encoding = 'gbk')
cards = np.array(df).tolist()
cards_json = []
for c in cards:
    cards_json.append(read_card(c))

data = json.dumps(cards_json)
f2 = open("/Users/Yuzhe/Desktop/cards.json",'w')
f2.write(data)
f2.close()