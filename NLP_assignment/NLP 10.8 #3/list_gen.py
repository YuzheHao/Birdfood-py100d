from func import *

def gen(path,namelist,nameo):
    fo = open(path+nameo,'a+')
    for names in namelist:
        fi = open(path+str(names))
        for line in tqdm(fi):
            print(line,file=fo,end='')
        fi.close()
    fo.close()



def main():
    me = 'Make it worth.'

    path = '/Users/Yuzhe/work/set2/'

    num = [
        [0,1,2,3,4],
        [1,2,3,4,0],
        [2,3,4,0,1],
        [3,4,0,1,2],
        [4,0,1,2,3],
    ]
    i=0
    for elem in num:
        namelist = []
        namelist2 = []
        namelist.append('sublist_'+str(elem[0]))
        for nums in elem[1:]:
            namelist2.append('sublist_'+str(nums))
        gen(path, namelist, 'test_'+str(i))
        gen(path, namelist2, 'train_'+str(i))
        i+=1


if __name__ == '__main__':
    main()