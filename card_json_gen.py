import re

def gen_list(txt_path):
    f = open(txt_path)
    all = []
    one = []
    for line in f:
        if line != '\n':
            txt = line.strip('\n')
            if txt[0] == '【':
                all.append(one)
                one = []
            one.append(txt)
    all.pop(0)
    return all

def gen_cards_info(txt_path):
    data_list = gen_list(txt_path)
    title_part = r'【(.*?)】'
    id_part = r'｜(.*?)｜'
    cards = []
    for data in data_list:
        card = {}
        card['title'] = re.findall(title_part, data[0])[0]
        card['series_id'] = str('%02d' % int(re.findall(id_part, data[0])[0].split('-')[0]))
        card['card_id'] = str('%03d' % int(re.findall(id_part, data[0])[0].split('-')[1]))
        card['description'] = '<br>'.join(data[1:])
        cards.append(card)
    return cards

txt_path = '/Users/Yuzhe/Desktop/饭盘子/goldrose.txt'
cards = gen_cards_info(txt_path)
f_out = open('./output.txt','w')
for card in cards:
    print('{\
"series_id": "%s",\
"card_id": "%s",\n\
"title": "%s",\
"message": "",\
"description": "%s",\
"series": "%s®",},'
          % (card['series_id'],
           card['card_id'],
           card['title'],
           card['description'],
           'GoldRose'),file=f_out)