from tqdm import tqdm

def delete_space_char(path_file):
    f = open(path_file)
    fnew = open(path_file + '_new','w')
    for line in tqdm(f):
        print(line.strip(' '),file=fnew,end='')
    f.close()
    fnew.close()

def delete_empty_line(filepath):
    f = open(filepath)
    fnew = open(filepath + '_new','w')
    for line in tqdm(f):
        data = line.strip('\n')
        if len(data) != 0:
            fnew.write(str(data))
            fnew.write('\n')
    f.close()
    fnew.close()

def txt_to_list(path,mode):
    list = []
    f = open(path)
    if mode == 'train':
        for line in f:
            data = line.strip('\n').split(' ')
            list.append(data)
            f = open(path)
        # -------------------------------
        # spec: transform num str to int
        for elem in list:
            elem[0] = int(elem[0])
        #--------------------------------
    if mode == 'test':
        for line in f:
            data = line.strip('\n').split(' ')
            list.append(data)
    f.close()
    return list

def run(train,test):
    bk = []
    for line in tqdm(test):
        if line[0] != '':
            bk = []
            for i in range(len(train)):
                if line[0] == train[i][1]:
                    bk.append(train[i])
            bk.sort(key=lambda x:x[0],reverse=True)
        if len(bk)!= 0:
            line.append(bk[0][2])
        else:
            line.append('NN')

def list_to_txt(list,num):
    f = open('/Users/Yuzhe/work/data/result_'+str(num),'w+')
    for line in list:
        strs = ''
        for elem in line:
            strs = strs +str(elem)+' '
        print(strs,file=f)
    f.close()



def main():
    me = 'Make it worth.'

    # 去除末尾的空格
    # for i in range(5):
    #     f = open('/Users/Yuzhe/work/data/result_'+str(i))
    #     fnew = open('/Users/Yuzhe/work/data/result_processed_'+str(i),'w+')
    #     for line in f:
    #         print(len(line))
    #         if line[0] == ' ':
    #             line = ''
    #         else:
    #             line = line[0:(len(line)-2)]
    #         print(line,file=fnew)
    #     f.close()
    #     fnew.close()

    # 去除行首的空格
    # for i in range(5):
    #     delete_space_char('/Users/Yuzhe/work/data/trained_'+str(i))


    for i in range(5):
        list_train = txt_to_list('/Users/Yuzhe/work/data/result_processed_'+str(i),'test')
        right = 0
        for line in tqdm(list_train):
            if len(line) > 2:
                if line[1] == line[3]:
                    right += 1
        print("Exp.%d ---> Accuracy: %f" % (i,right/len(list_train)))






if __name__ == '__main__':
    main()