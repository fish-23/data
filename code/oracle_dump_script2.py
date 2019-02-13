#!/usr/local/python3
# -*- coding: UTF-8 -*-


# 没有外键关系的数据库
# 处理空值问题

import cx_Oracle as oracle
import collections as co

def save_data(table,values):
    db=oracle.connect('wlp/wlp@127.0.0.1:1521/orcl')
    c=db.cursor()
    for i in values:
        x = co.deque([])
        for j in i:
            if j == None:
                j = ' '
            x.append(j)
        x = tuple(list(x))
        c.execute("insert into %s values %s"%(table[0],x))
    c.close()
    db.commit()
    db.close()
    return(1)

def find_data():
    db=oracle.connect('ht/ht@127.0.0.1:1521/orcl')
    c=db.cursor()
    c.execute("select table_name from user_tab_comments where table_type = 'TABLE'")
    table_all=c.fetchall()
    for table in table_all:
        c.execute("select * from %s where rownum <= 3"%(table[0]))
        info = c.fetchall()
        if info == []:
            continue
        save_data(table,info)
    c.close()
    db.close()
    
def start():    
    find_data()

if __name__ == '__main__':
    start()

