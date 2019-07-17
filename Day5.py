'''
F: 检测一个数是否为水仙花数
I/O: 直接运行函数执行结构
'''
def shuixianhua_check():
    target = int(input("请输入待测数字："))
    print("请确认所输入数字为：%d" % target)
    while():
        if (target<100 or target>=1000):
            print("要求输入三位数，请重新输入")
            target = int(input("请再次输入待测【三位数】："))
        else:
            break
    e2 = target // 100
    e1 = (target % 100) // 10
    e0 = target % 10
    if (e0**3+e1**3+e2**3==target):
        print("数字 %d 是水仙花数" % target)
    else:
        print("数字 %d 不是水仙花数" % target)

# python的main函数入口方式
if __name__ == '__main__':
    ops=['shuixianhua_check()']
    print("可执行函数有：")
    for i in range (len(ops)):
        print("---> ", end="")
        print(ops[i])
