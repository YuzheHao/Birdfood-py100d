import numpy as np
import os

def LOADING(DATA):
    file = open(DATA,'r')
    out = []
    for line in file:
        if line[0] != '#':
            out.append(list((line.strip('\n').split(' '))))
    out2 = []
    for e1 in out:
        ins = []
        e1[0] = round(float(e1[0]))
        for e2 in e1:
            ins.append(float(e2))
        out2.append(ins)
    return out2

def s(lmd):
    c = 299792458
    h = 6.6260755e-34
    e = 2.71828182846
    kb = 1.380658e-23
    T = 6504
    sx = 2*c*c*h/(lmd**5*(e**((h*c)/(kb*T*lmd))-1))
    return(sx)

def K_calcu(xyz,pig):
    sums = 0
    # print(xyz)
    for elem in pig:

        unit = s(elem[0]) * xyz[int(elem[0])-400][1]
        sums = sums + unit
    sums = 1/sums
    return sums

def get(pig_index,pig,xyz,K,pos):
    sums = 0
    for lmd in pig_index:
        r = pig[pig_index.index(lmd)][1]
        xx = xyz[int(lmd)-400][pos]
        # print("s: ",s(lmd))
        # print("r:", r)
        # print("xx", xx)
        unit = s(lmd)*r*xx
        # print("unit: ",unit)
        # print("-------------------")
        sums += unit
    sums = sums * K
    return sums

def judge(r1):
    if r1 < 0.0031308:
        r2 = r1 * 12.92
    else:
        r2 = 1.055*r1**(1/2.4) - 0.055
    return r2

def cut(x):
    if x < 0:
        x = 0
    elif x > 1:
        x = 1
    else:
        x = x
    return x


xyz = LOADING("/Users/Yuzhe/Desktop/XYZ_CIE_2.dat")
xyz = xyz[20:320]

plots = ['1','6','15','33','41','46','51','58','64','72','74','84','92']
# plots = ['1']
for num in plots:
    pig = LOADING("/Users/Yuzhe/Desktop/Pigmentdata/"+num+"plot")

    K = K_calcu(xyz,pig)
    # print(K)

    pig_index = []
    for elem in pig:
        pig_index.append(elem[0])

    x = get(pig_index,pig,xyz,K,1)
    y = get(pig_index,pig,xyz,K,2)
    z = get(pig_index,pig,xyz,K,3)
    print("Now processing: Plot",num)
    print("XYZ cord: ",x,y,z)

    r1 = cut(3.2406*x + -1.5372*y + -0.4986*z)
    g1 = cut(-0.9689*x + 1.8758*y + 0.0415*z)
    b1 = cut(0.0557*x + -0.2040*y + 1.0570*z)
    print("1: ",r1,g1,b1)

    r2 = judge(r1)
    g2 = judge(g1)
    b2 = judge(b1)
    print("2: ",r2,g2,b2)

    r3 = round(255*r2)
    g3 = round(255*g2)
    b3 = round(255*b2)

    print("RGB 8bits cord: ",r3,g3,b3)
    print("-----------------")

    print(K)
