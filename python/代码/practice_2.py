#!/usr/bin/python
# -*- coding:utf-8 -*-


x = '练习1'
y = x.decode('utf-8')
z = y.encode('gbk')
print z 
print '有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？'
print '(1)'
'''
d = []
d2 = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (j <> k) and (i <> k) and (i <> j):
                print i*100+j*10+k
                d.append([i,j,k])
                d2 += 1
x = '总数量:'
y = x.decode('utf-8')
z = y.encode('gbk')
print z,
print len(d),d2,
'''
print'(2)'
list_num = [1,2,3,4]
list  = [i*100 + j*10 + k for i in list_num for j in list_num for k in list_num if (j != i and k != j and k != i)]
print list
x = '组成的三位数数量:'
y = x.decode('utf-8')
z = y.encode('gbk')
print z,len(list)
print '\n'
print



x = '练习2'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？'
print
#  profit利润, Commission提成，bonus奖金
p = raw_input('请输入利润:\n')
p = long(p)
bon = 0
pro = [1000000,600000,400000,200000,100000,0]
com = [0.01,0.015,0.03,0.05,0.075,0.1]
for i in range(0,6):
    if p >= pro[i]:
        bon += com[i] * (p-pro[i]) #bon为两次相加的结果，所以为 +=
        p = pro[i]   
print bon
print '\n'
print




x = '练习3'
y = x.decode('utf-8')
z = y.encode('gbk')
print z          
print '一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？'
# 设这个数为x, x + 100 = n**2, x + 100 + 168 = m**2, m**2 - n**2 = 168
# (m+n)*(m-n) = 168, 1<(m+n)<168, 1<(m-n)<168, 前面两式相加得，1<m<168
# 想减得， 1<n<168
            
for m in range(1,169):
    for n in range(1,m):
        if (m+n)*(m-n)==168: #在for中,m永远大于n, n和m互换位置后，此等式永远为负
            x=n**2-100
            t = '符合条件的整数有:'
            y = t.decode('utf-8')
            z = y.encode('gbk')
            print z, x          
print '\n'
print




x = '练习4'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '输入某年某月某日，判断这一天是这一年的第几天？'
'''
dic = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
def time(y,m,d):
    day = 0
    j = i = m
    for i in range(1,j):
        if y % 4 == 0:
            if m <= 2:
                day += dic[i]
            else:
                dic[2] = 29
                day += dic[i]
                i += 1
        else:
            day += dic[i]
            i += 1
    print (day + d)
y = int(raw_input('请输入年：'))
m = int(raw_input('请输入月：'))
d = int(raw_input('请输入日：'))
time(y,m,d)
'''
print '\n'
print


           

x = '练习5'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '输入三个整数x,y,z，请把这三个数由小到大输出。'

print'(1)排序函数 sort() 的用法, 用for循环输入三个数'
print '*^*_*^*_*^*_*^*_*^*_*^*_*^*_*^*_*^*_*^*_*^*_*^*'
'''
lis = []
for i in range(3):
    x = int(raw_input('输入三个参数：\n'))
    lis.append(x)
print lis
lis.sort()
print lis
'''
print
x = '(2)冒泡序列'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
# sequence序列
def sequence(lis):
    for i in range(len(lis)):
        for i in range(len(lis)-1):
            if lis[i] > lis[i+1]:
                lis[i] = lis[i] + lis[i+1]
                lis[i+1] = lis[i] - lis[i+1]
                lis[i] = lis[i] - lis[i+1]
                i += 1
    print lis
sequence([11,5,2,0,8])

def sequence(lis):
    for i in range(len(lis)):
        for i in range(len(lis)-1):
            if lis[i] < lis[i+1]:
                lis[i] = lis[i] + lis[i+1]
                lis[i+1] = lis[i] - lis[i+1]
                lis[i] = lis[i] - lis[i+1]
                i += 1
    print lis
sequence([11,5,2,0,8])
print '\n'
print



x = '练习6'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '斐波那契数列'
print '-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-'
print '\n'
print




x = '练习7'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '将一个列表的数据复制到另一个列表中。'
x = [1,2,3]
y = x
print y

x = [1,2,3]
y = x[:]
print y

x = [1,2,3]
y = []
for i in range(len(x)):
    y.append(x[i])
print y
print '\n'
print



x = '练习8'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '输出 9*9 乘法口诀表'
for i in range(1,10):
    print                    # 会在一行后输入回车一次
    for j in range(1,i+1):
        print '%d*%d =%d '%(j,i,j*i), # print 结束时加上逗号，结果会显示在一行
        #print '{}*{}={}'.format(j,i,j*i),
print '\n'
print





x = '练习9'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '使用 time 模块的 sleep() 函数,暂停一秒输出.'
import time
lis = [1,2,3]
for i in range(len(lis)):
    print lis[i]
    time.sleep(0.01) #暂停两秒后输出
print '\n'
print




x = '练习10'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '暂停一秒输出，并格式化当前时间。'
import time
time.sleep(0.01)
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print '\n'
print





x = '练习11'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？'
print '-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-'
print '\n'
print





x = '练习12'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '判断99-200之间有多少个素数，并输出所有素数'
lis = []
for i in range(99,201):
    for j in range(2,i):
        if i % j == 0:
            break
        else:
            if j == i-1:
                lis.append(i)
print lis
print '\n'
print






x = '练习13'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。'
print '方法一'
for x in range(10):
    for y in range(10):
        for z in range(10):
            w = x*100 + y*10 + z
            if (w>100) and (w == x**3 + y**3 + z**3):
                print w,
print
print '方法二'
for n in range(100,1000):
    x = n/100
    y = n/10 % 10
    z = n % 10
    n1 = pow(x,3) + pow(y,3) + pow(z,3)
    if n == n1:
        print n,
print '\n'
print





x = '练习14'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。'
def num(intl):
    lis = []
    intl1 = intl
    if not isinstance(intl,int) or intl<=0:
        while True:               # 可以用exit(),来结束程序
            return '请输入一个正确的正整数' 
    else:
        while intl > 1:
            for i in range(2,n+1):
                if intl % i == 0:
                    intl = int(intl/i) #这里为赋， ==为判断符号，判断是否相等
                    lis.append(i)
                    break
    lis = "*".join([str(x) for x in lis])
    # '[1,2,3]'字符串列表，不适合join，['1','2','3'],适合join
    return '{0} = {1}'.format(intl1,lis)
print num(-90)
print num(90)
print '\n'
print  
            





x = '练习15'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。'
def score(intl):
    if isinstance(intl,int) and intl >= 0:
        if intl in range(90,101):
            print '{} is A'.format(intl)
        elif intl  in range(60,90):
            print '{} is B'.format(intl)
        else:
            print '{} is C'.format(intl)
    else:
        print '请输入正确的成绩'
score(95),score(55),score(80),score(-80)
print '\n'
print






x = '练习16'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '输出指定格式的日期'
import time
print time.time()  #1498539133.655
print time.localtime()  #tm_year=2017, tm_mon=6, tm_mday=27, tm_hour=12, tm_min=53, tm_sec=16, tm_wday=1, tm_yday=178, tm_isdst=0
print time.asctime()  #'Tue Jun 27 12:53:50 2017'
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()) #'2017-06-27 13:00:57'
import datetime
print datetime.date.today() #datetime.date(2017, 6, 27)
print datetime.date.today().strftime('%d/%m/%Y') #'27/06/2017'
print datetime.date(1941, 1, 5) #datetime.date(1941, 1, 5)
print '\n'
print





    
x = '练习17'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数'
# letters字母，space空格，digit数字
def choice(strl):
    lis_letter = []
    lis_apace = []
    lis_digit = []
    lis_other = []
    for i in strl:
        if i.isalpha():   # 检测字母
            lis_letter.append(i)
        elif i.isspace(): # 检测空格
            lis_apace.append(i)
        elif i.isdigit(): # 检测数字
            lis_digit.append(i)
        else:             # 检测其他
            lis_other.append(i)
    print 'letter = {0} = {1}'.format(len(lis_letter),lis_letter)
    print 'apace = {0} = {1}'.format(len(lis_apace),lis_apace)
    print 'digit = {0} = {1}'.format(len(lis_digit),lis_digit)
    print 'other = {0} = {1}'.format(len(lis_other),lis_other)
choice('12345  asdfg  +-*/! ')
print '\n'
print




x = '练习18'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。'
def num(x,n):           
    lis = []
    sum = 0
    Tn = 0
    for i in range(n):
        Tn = Tn + x
        x = x * 10
        lis.append(Tn)
        sum += Tn
        print Tn
    print lis, '\n', 'sum =', sum
# x:数字,n:几个数相加
num(3,5)
print '\n'
print        
        
        
        
        


x = '练习19'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数'
# different差值, result结果, perfect_number完数
for i in range(2,1001):
    different = i
    for j in range(1,i):
        if i % j == 0:
            different -= j
    if different == 0:
        lis = []
        perfect_number = i
        for j in range(1,i):
            if i % j == 0:
                lis.append(j)
        result = '+'.join(str(x) for x in lis)
        print '{0} = {1}'.format(perfect_number,result)


for i in range(5,7):
    s = i
    lis = []
    for j in range(1,i):  #当循环缺少range时无法运行
        if i % j == 0: #不能用s，s是变量，当s-1后就成了5，会出错
            s -= j
            lis.append(j)
    if s == 0:
        print '{} = {}'.format(i, "+".join(str(x) for x in lis))
print '\n'
print       







x = '练习20'
y = x.decode('utf-8')
z = y.encode('gbk')
print z    
print '一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？'
h = 100.0
lis = [-100]
for i in range(1,11):
    lis.append(2*h)
    h = h/2
print 'sum_10 = ',sum(lis)
print 'h = ', h
print '\n'
print    

            


            

x = '练习21'
y = x.decode('utf-8')
z = y.encode('gbk')
print z  
print '猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少'
x2 = 1
for i in range(9,0,-1):
    x1 = (x2+1)*2
    x2 = x1
print
print x1
print '\n'
print





x = '练习22'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。'
for a in ('x','y','z'):
    for b in ('x','y','z'):
        for c in ('x','y','z'):
            if (a!=b) and (a<>c) and (b<>c) and (a<>'x') and (c<>'x') and (c<>'z'):
                print 'a = {0}, b = {1}, c = {2}'.format(a,b,c)
print '\n'
print







x = '练习23'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
x = '打印菱形'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
from sys import stdout
for i in range(4):
    for j in range(4-i-1):
        print ' ',          # 因为有逗号，输出中会有空格
        # stdout.write(' ')   这样输出中间无空格
    for k in range(1+i*2):
        print '*',
        # stdout.write('*')
    print
for i in range(1,4):
    for j in range(i):
        print ' ',
    for k in range(7-i*2):
        print '*',
    print
print
print '*^*_*^*_*^*_*^*_*^*_*^*_*^*_*^*_*^*_*^*_*^*_*^*'
print
def num(n):
    for i in range(n):
        a = abs(i - int(n/2))
        b = n - 2*a
        print ' '*a + '*'*b
num(7)

print '\n'
print


            
        
x = '练习24'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和'
a = 2.0
b = 1.0
c = 0
s = 0
for i in range(20):
    s += a/b
    c = a
    a = a+b
    b = c
print s
print '\n'
print
    
    
         



x = '练习25'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '求1+2!+3!+...+20!的和'
s = 0
x = 1
for i in range(1,21):
    x *= i
    s += x
print s
print '\n'
print        
    





x = '练习26'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '利用递归方法求5!'
print '-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-'
print '\n'
print





x = '练习27'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来'
print '-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-'
print '\n'
print





x = '练习28'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？'
x = 10
for i in range(4):
    x += 2
print x
print '\n'
print        






x = '练习29'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字'
def  num(strl):
    l = len(str(strl))
    lis = []
    for i in range(l):
        x = strl % 10
        strl /= 10
        lis.append(x)
    print "长度为：{0}, \n逆序为:{1}".format(l,''.join(str(x) for x in lis) )
num(123)
print '\n'
print 




x = '练习30'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同'
def num(strl):
    if (strl / 10000) == (strl % 10):
        if ((strl / 1000) % 10) == ((strl % 100) / 10):
            if ((strl / 100) % 10) == ((strl / 1000) % 10 + 1) == ((strl % 100) / 10 + 1):
                print '{} is True'.format(strl)
            else:
                print '{} is False'.format(strl)
        else:
            print '{} is False'.format(strl)
    else:
        print '{} is False'.format(strl)
num(12321),num(12421)
print
def num(intl):
    x = str(intl)
    for i in range(len(x)):
        if x[i] == x[(-i)-1]:
            if int(x[(i/2)])+1 == int(x[(i/2 +1)]) == int(x[(i/2 +2)])+1:
                print '{} is True'.format(intl)
                '''
            else:
                print '{} is False'.format(intl)
        else:
            print '{} is False'.format(intl)
'''    
num(12321),num(12421)
print '\n'
print





x = '练习31'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母'
dic1 = {M:momday, W:wednesday, F:friday}
dic2 = {Tu:Tuesday, Th:Thursday, Sa:Saturday, Su:Sunday}
def num(strl):
        
    



        
        








































