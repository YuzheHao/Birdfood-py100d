'''
----------------------------------------
2019-4-20 16:31
【目前状态】
+ 主要功能
- 不足之处
? 尚未解决的问题
----------------------------------------
'''

import datetime
import os

'''[读取一个目录下的所有文件的名字]
    <I>: 目录所在路径（如下实例所示）
    <O>: 有多种可选项输出'''
def name_read(cwd):
    # 路径例子：cwd = 'E:\\burgerking\\dataset_image\\tfr_multi\\'
    dir = os.listdir(cwd)
    #name_list={}
    for names in dir: # file相当于一个新创的变量，用来承载该目录下的文件的名字
        print(names)
      #name_list.append(names)
    #return(name_list)

'''[程序结束的时间戳]
    <直接使用>'''
def TIMESTAMP_POST():
    time_now = datetime.datetime.now().strftime('%F_%H-%M-%S_CST')
    cc_0,cc_1 = "\033[0;36m","\033[0m"
    print(cc_0+"--------------------------")
    print("<程序结束>")
    print("<"+time_now+">")
    print("--------------------------"+cc_1)

'''[将print输出到外部txt文本中]
    <I>: txt文件所在路径、需要输出的文本（都是字符串）'''
def write_txt(_PATH, _TEXT):
    # _PATH例子："E:/HYZ/NB.TXT"
    # _TEXT例子："even dead, i am the hero"
    _FILE = open(_PATH, 'a')
    print(_TEXT, file=_FILE)
    _FILE.close()

'''[检索特定字符在待检测字符串中的位置索引]
    <I>: (待检测字符串、待检测字符)
    <O>: 索引编号'''
def get_char_pos(string, char):
    chPos = []
    try:
        chPos = list((pos for pos, val in enumerate(string) if (val == char)))
    except:
        pass
    out = chPos[0]
    return out