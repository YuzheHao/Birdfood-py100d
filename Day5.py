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

'''
F: 因数分解、检测一个数是否为完美数
I/O: 直接运行函数执行结构
'''
def wanmei_check():
    target = int(input("请输入待测数字："))
    print("请确认所输入数字为：%d" % target)
    factor=[]
    # 因数分解部分
    for i in range(target-1):
        if (target % (i+1) == 0):
            factor.append(i+1)
    # 除自身外的因数相加部分
    sum = 0
    for i in factor:
        sum = sum + i
    # 完美数判定部分
    if (sum == target):
        print("所输入的数字 %d 是完美数" % target)
        flag =1
    else:
        print("所输入的数字 %d 不是完美数" % target)
        flag=0
    # 输出完美数的加法结构
    if (flag==1):
        print("%d = " % target,end="")
        for i in factor:
            if (i != factor[len(factor)-1]):
                print(i,end="")
                print(" + ",end="")
            else:
                print(i,end="")


# python的main函数入口方式
if __name__ == '__main__':
    ops=['shuixianhua_check()','wanmei_check()']
    print("可执行函数有：")
    for i in range (len(ops)):
        print("---> ", end="")
        print(ops[i])
    # 还缺一个input和switch语句来选择执行的程序
