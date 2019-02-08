# 存数据函数
def save_data(table,values):
    db=oracle.connect('wlp/wlp@127.0.0.1:1521/orcl')
    c=db.cursor()
    for i in values:
        print(i)
        print(type(i))
        c.execute("insert into %s values %s"%(table,i))
    c.close()
    db.commit()
    db.close()
    return(1)


# 一，链接
#引用模块cx_Oracle
import cx_Oracle as oracle
#连接数据库
db=oracle.connect('ht/ht@127.0.0.1:1521/orcl')
# 获取游标
c=db.cursor()


# 二，查表结构
# 查出所有的表
c.execute("select * from user_tab_comments where table_type = 'TABLE'")
table_all=c.fetchall()
dic = {}
values_table = []
for i in range(len(table_all)):
    lis = []
    table = table_all[i][0]
    # 查询出所有外键信息
    c.execute("select * from user_constraints c where c.constraint_type = 'R' and c.table_name=upper('%s')"%table)
    foreign_key=c.fetchall()
    if foreign_key == []:
        dic[table] = []
    else:
        for j in foreign_key:
            table_sid = j[1]
            m_table_sid = j[6]
            # 查询出所有外键信息对应的表情况
            c.execute("select * from user_cons_columns cl where cl.constraint_name =upper('%s')"%m_table_sid)
            foreign_key2=c.fetchall()
            # 取出表名,外键对应的字段名
            m_table = foreign_key2[0][2]
            m_column_name = foreign_key2[0][3]
            #取出字表对应的字段
            c.execute("select * from user_cons_columns cl where cl.constraint_name =upper('%s')"%table_sid)
            foreign_key3=c.fetchall()
            column_name = foreign_key3[0][3]
            foreign_info = column_name + '-' + m_table + '-'+ m_column_name
            values_table.append(m_table)
            lis.append(foreign_info)
        dic[table] = lis

#print('1，打印出所有的表及其对应的母表')
#print(dic)
set_dic = set(dic)
#print('2，使用set方法，取出所有字典的键')
#print(set_dic)
for key in values_table:
    if key in set_dic:
        dic.pop(key)
print('3，打印出最顶端的母表')
print(dic)


# 三，存数据
for table in  dic:
    # 查询主键编号
    c.execute("select index_name  from user_constraints c where c.constraint_type = 'P' and c.table_name=upper('%s')"%table)
    index_name_num = c.fetchall()[0][0]
    # 查询主键
    c.execute("select * from user_cons_columns cl where cl.constraint_name =upper('%s')"%index_name_num)
    index_name = c.fetchall()[0][3]
    foreign_dic = {}
    for m_table_index_info in dic[table]:
        m_table_index_info = m_table_index_info.split('-')
        print(m_table_index_info)
        # 查询3条数据对应的母表的主键
        #c.execute("select %s from %s  where rownum <= 3 order by %s desc"%(m_table_index_info[0],table,index_name))
        x = c.execute("select %s from %s  where rownum <= 3 "%(m_table_index_info[0],table))
        m_table_id = c.fetchall()
        m_table_id = [i[0] for i in m_table_id]
        m_table_id = tuple(set(m_table_id))
        foreign_dic[m_table_index_info[0]] = m_table_id
        # 通过主键查询出母表数据
        c.execute("select * from %s where %s in %s"%(m_table_index_info[1],m_table_index_info[2],m_table_id))
        m_table_data = c.fetchall()
        print(m_table_data)
        save_data(m_table_index_info[1],m_table_data)
    foreign_key = list(foreign_dic.keys())
    c.execute("select * from %s where rownum <= 3 and %s in %s"%(table,foreign_key[0],foreign_dic[foreign_key[0]]))
    info = c.fetchall()
    save_data(table,info)
c.close()
db.close()
