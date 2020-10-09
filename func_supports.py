import os

def read_files_in_path(work_path,target_affix='',INGORE_HIDDEN=True):
    files, dirs = [], []
    for f in os.listdir(work_path):
        if os.path.isdir(work_path + f):
            dirs.append(f)
        else:
            if target_affix == '':
                files.append(f)
            elif f[-3:].lower()==target_affix:
                files.append(f)
    files = [f for f in files if not f[0] == '.']
    dirs = [d for d in dirs if not d[0] == '.']
    files.sort()
    dirs.sort()
    return files,dirs

# f,d = read_files_in_path('/Users/Yuzhe/Experiments/2020100501/',target_affix='mov')
# print(f)
# print(d)