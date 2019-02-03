# -*- coding: utf-8 -*-
#!/usr/bin/env python


# 读文件，一行一行读取文件
import time 
with open('1.txt','r') as file:
    while 1:
        line = file.readline()
        print(line)
        time.sleep(1)
        if not line:
            break
        pass # do something
    print('end')


# 读写文件，读取文件后给每行加序号后写入另外一个文件
with open(r'1.txt') as f1:
    file1 = f1.readlines()
    for i in range(len(file1)):
        file1[i] = str(i+1) + '.' + '  ' + file1[i]
with open(r'2.txt','a') as f2:
    f2.writelines(file1)
