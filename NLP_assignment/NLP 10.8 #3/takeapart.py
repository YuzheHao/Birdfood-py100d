from func import *

def apart(pathi,patho):
    cnt1 = 0
    cnt2 = 0
    f = open(pathi)
    for line in tqdm(f):
        if cnt1 == 52000 and cnt2 != 3:
            cnt1 = 0
            cnt2 += 1
        fo = open(patho+'sublist_'+str(cnt2),'a+')
        print(line,file=fo)
        fo.close()
        cnt1 += 1
    f.close()





def main():
    me = 'Make it worth.'
    
    # pathi = '/Users/Yuzhe/work/set2/train.txt'
    # patho = '/Users/Yuzhe/work/set2/'
    # apart(pathi,patho)
    #
    # path = '/Users/Yuzhe/work/set2/'
    # list = 'sublist_'
    # delete_empty_line(path+'test.txt')











if __name__ == '__main__':
    main()