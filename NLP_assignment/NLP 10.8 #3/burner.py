from func import *

for i in range(1,5):
    print(i)
    list_train = txt_to_list('/Users/Yuzhe/work/data/trained_'+str(i)+'_new','train')
    list_test = txt_to_list('/Users/Yuzhe/work/data/test_'+str(i),'test')
    # list_test = [[',', ',', 'O']]
    run(list_train,list_test)
    list_to_txt(list_test,i)

