import os

def process(str):
    l = str.split(' ')
    stamps = l
    stamps[0] = '{:0>4d}'.format(int(l[0][:len(l[0])-1]))
    stamp = '_'.join(stamps)
    return stamp

n = '107. Binary Tree Level Order Traversal II'
print(process(n))

# if __name__ == '__main__':
#     work_path = '/Users/Yuzhe/Documents/projects/py/birdfood/leetcode/'
#     for path,dir_list,file_list in os.walk(work_path):
#         files = [f for f in file_list if not f[0] == '.']
#         for f in files:
#             if f[:2]!='00':
#                 print(f)
#                 print(process(f))
#                 os.rename(work_path+f, work_path+process(f))
#                 print('----')

