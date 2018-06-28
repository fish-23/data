# -*- coding: utf-8 -*-
#!/usr/bin/env python
from peewee import *


def child(parent_id,lis):
        lis2 = []
        lis3 = []
        for i in parent_id:      
            ret = UserNetworks.select().where(UserNetworks.parent == i)
            if ret.count() != 0 :      
                 lis2.append(i)
                 for j in ret:
                     lis3.append(j.owner.id)
        if len(lis2) == 0:
            l = 0
            for i in lis:
                x = len(i)
                l += x
            child_info = {'count':l,'lis':lis}
            return child_info
        lis.append(lis3)
        child(lis3,lis)


def parent(chind_id, lis, i):
        if i == 0:
            parent = UserNetworks.select().where(UserNetworks.owner == chind_id)
            if parent.count() == 0:
                parent_info = {'count':0,'lis':[]}
                return parent_info
        parent = UserNetworks.select().where(UserNetworks.owner == chind_id)
        if parent.count() == 0:
            l = len(lis)
            parent_info = {'count':l,'lis':lis}
            return parent_info
        parent_id = UserNetworks.get(UserNetworks.owner == chind_id).parent.id
        lis.append(parent_id)
        i = 1
        parent(parent_id, lis, i)
        
        
def start():        
        start_id = '3'
        lis =[]
        parent_id = [start_id]
        child_info = child(parent_id,lis)
        child_id = [start_id]
        i = 0
        parent_info = parent()
        print child_info,parent_info
            
if __name__ == "__main__":
	    start()  
