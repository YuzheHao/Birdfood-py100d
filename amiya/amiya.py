import cv2
import numpy as np
import os
import math
from matplotlib import pyplot as plt
from tqdm import tqdm

def del_file_suffix(string):
    for i in range(len(string)):
        if string[-(i+1)] == '.':
            return string[:-(i+1)]
    print('[ERROR] NO SUFFIX FOUND FOR THE INPUT STRING : "%s" !' % string)

def read_files_in_path(work_path,show_hidden=False):
    if work_path[-1]!='/': work_path += '/'
    if work_path[0]!='/': work_path = '/' + work_path
    files, dirs = [], []
    for f in os.listdir(work_path):
        if os.path.isdir(work_path + f):
            dirs.append(f)
        else:
            files.append(f)
    if not show_hidden:
        files = [f for f in files if not f[0] == '.']
        dirs = [d for d in dirs if not d[0] == '.']
    files.sort()
    dirs.sort()
    return files,dirs

def magic_draw(y,
    x = None,
    fig_size = (15,6),
    fig_title = None,
    x_label = None,
    y_label = None,
    color_code = None,
    colors = ['deepskyblue','orange','limegreen','#C82B46','#4EA089','#8B77D0','#93613A','#A5CC4F'],
    alpha = 0.87
    ):

    plt.figure(figsize=fig_size)
    plt.grid()
    plt.title(fig_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # if multiple input:
    if type(y[0]) == list:
        pics_num = len(y)
        if pics_num > 8:
            print('[ERROR] picture are too many to draw! (max 8 but got %d)' % pics_num)
            return
        # if no input x-coordinate situation:
        if not x:
            x = []
            for data in y:
                x.append(range(len(data)))
        for i in range(pics_num):
            plt.plot(x[i],y[i],alpha=alpha,color=colors[i])

    # if single input:
    else:
        # if no input x-coordinate situation:
        if not x: x = range(len(y))
        # if no color requirement:
        if not color_code:
            color = colors[0]
        # if has requiremnet for color:
        else:
            if type(color_code) == str:
                color = color_code
            elif type(color_code)==int and (color_code>=0 and color_code<=7):
                color = colors[color_code]
            else:
                print('[ERROR] color code went wrong, automatically choose default.')
        plt.plot(x, y, alpha=alpha, color=color)

    plt.show()






















