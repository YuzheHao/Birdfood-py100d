# README

### template(`input_arg`, *default_arg*)

#### ---> input (1):
* arg#1 `input_arg` (type): explanation.  
* arg#2 `default_arg=default_value` (type): explanation.

#### ---> output (1):
* return (type): explanation.
* more memo

#### ---> example:
``````python
>>>

``````
----

### read_files_in_path(`work_path`, *show_hidden*)

#### ---> input (2)：  
* arg#1 `work_path`  (string): a path string, where the files you want to read are in.  
* arg#2 `show_hidden=False` (bool): a flag bool, if it is *False*, the hidden file will be ignored.   

#### ---> output (2)：  
* return#1 `files` (list): a list of strings, which are the names of all files in this path.  
* return#2 `dirs`(list): a list of strings, which are the names of all directories in this path.  
* the returned list have been sorted:  `List.sort()`

#### ---> example:
``````python
>>> files, dirs = read_files_in_path('/User/amiya/Desktop/')
>>> files
['map.jpg','memo.txt','video_tape.mp4']
>>> dirs
['album','resume','normal_files',]

>>> files, dirs = read_files_in_path('/User/amiya/Desktop/',show_hidden=True)
>>> files
['map.jpg','video_tape.mp4','memo.txt','.chen.doc']
>>> dirs
['normal_files','album','resume','.elite_resume']
``````

----

### del_file_suffix(`string`)

#### ---> input (1)：  
* arg#1 `string` (string): a string needed to remove its suffix (usually to be a file name).  

#### ---> output (1)：  
* return (string): the string after the suffix is removed.  

#### ---> example:
``````python
>>> after = del_file_suffix('password_book.txt')
>>> after
'password_book'

>>> after = del_file_suffix('password_book')
>>> after
#print: [ERROR] NO SUFFIX FOUND FOR THE INPUT STRING : "password_book" !
``````

----

### def magic_draw(`y`, *x*, *fig_size*, *fig_title*, *x_label*, *y_label*, *color_code*, *colors*, *alpha*)

#### ---> input (1):
* arg#1 `y`(List / Lists' List): list/several lists of data need to be draw. 
* arg#2 `x=range(len(y))` (List / Lists' List): list/several lists of x-coordinates, default as an one-by-one conuting list
* 

#### ---> output (1):
* return (type): explanation.
* more memo

#### ---> example:
``````python
>>>

``````
----
