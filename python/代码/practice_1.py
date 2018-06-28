#!usr/bin/python
# -*- coding:utf-8 -*-

print '练习一'
print '定义 is_Even 函数，传一 int 参数，判断是否是偶数'
def is_Even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print is_Even(8), is_Even(0), is_Even(-8),is_Even(1),is_Even(-3)
print '\n'





print '练习二'
print '定义 is_Int 函数，传一 float 参数，判断是否是整数（如1.0 即整数）'

'''
浮点数误差范围与数据类型相关
双精度（double型）一般为1e-15，单精度（float型）一般为1e-6
双精度对应1e-15和15个9（单精度对应1e-6和6个9）
'''
print 'C语言中'
def is_Int(i):
    if i >= 0:
        if (i - int(i) < 1e-15) | (i - int(i) > 0.999999999999999):
            return True
        else:
            return False
    else:
        if (-(i - int(i)) < 1e-15) | (-(i- int(i)) > 0.999999999999999):
            return True
        else:
            return False
print is_Int(4.000001),; print is_Int(-2.0000000)

print 'python中'
def is_Int(f):
    if(f%1 == 0):
        print True
    else:
        print False
is_Int(0),;is_Int(-1.0),;is_Int(1.0000000000000001)
print '\n'





print '练习三'
print '定义 digital_sum 函数，传一 int 参数，return 其所有位数的数字相加的和'

def digital_sum(i):
    l = 0
    suml = 0
    if i < 0:
        i = -i
    x = len(str(i))
    while l < x:
        l = l + 1
        j = i % 10
        suml = suml + j
        i = int(i/10)
    return suml
print digital_sum(234),digital_sum(-1224),digital_sum(76),digital_sum(0)


i = raw_input('请输入一个整数：\n')
i = int(i)
def digital_sum(i):
    dis = []
    sum = 0
    n = 0
    if i < 0:
        i = -i
    while i != 0:
        j = i % 10
        dis.append(j)
        i = int(i/10)
        sum = sum + dis[n]
        n = n + 1
    return sum
print digital_sum(i)

print '************************************'
def digital_sum(i):
    i = str(i)
    sum = 0
    for d in i:
        sum += int(d)
    return sum
print(digital_sum(23423),digital_sum(900),digital_sum(0))
print '************************************'
print '\n'





print '将字符串转化成列表'
def str_in(strl):
    strl = str(strl)
    dis = []
    i = 0
    j = 0
    l = len(strl) 
    while j < l:
        j = j + 1
        dis.append(strl[i])
        i += 1
    return dis
print str_in('asd')

print '练习四'
print '定义 factorial 函数，传一 int 参数，return 其所有位数数字相乘的积'
def factorial(intl):
    product = 1
    if intl < 0:
        intl = -intl
        for i in str(intl):
            product = product * int(i)
        return (-product)
    else:
        for i in str(intl):
            product = product * int(i)
        return product
print factorial(123),factorial(-124)
print '\n'




print '练习五'
print '定义 is_prime 函数，传一 int 参数，判断是否是质数'
def is_prime(intl):
    i = 2
    if intl == 2:
        return True
    elif intl > 2:
        if intl % 2 == 0:
            return False
        else:
            while i < intl:
                if intl % i == 0:
                    return False
                else:
                    i += 1
            return True
    else:
        return False
print is_prime(0),is_prime(1),is_prime(-58),is_prime(9),is_prime(2),is_prime(11)

print '************************************'
def is_prime(i):
    result = True
    for d in range(2,i):
        if(i%d==0):
            result = False
            break
    if(i==0):
        result = False
    return result        
print(is_prime(9),is_prime(2),is_prime(3),is_prime(4),is_prime(13),is_prime(197))

print '\n'




    
print '练习六'
print '定义 reverse 函数，传一 str 参数，将所有字符串字符倒置并 return 该字符串'
def reverse(strl):
    i = 0
    l = len(strl)
    j = len(strl) - 1
    suml = str()
    while i < l:
        i = i + 1
        suml = suml + strl[j]
        j = j - 1 
    return "'%s'" % suml
print(reverse('asd  fgh'))

def rewerse(strl):
    lis = []
    l = range(len(strl))
    j = len(strl) - 1
    for i in l:
        lis.append(j)
        j -= 1
    lis_1 = ''.join(lis)
    return lis_1
print(reverse('asd  fgh'))
print '************************************'
print ('将输出的字符串带上引号方法二，return repr(suml)')
print '************************************'
print '\n'




print '练习七'
print '定义 anti 函数，传一 str 参数，将字符串中所有的元音（a e i o u） 去除'
def anti(strl):
    x = 'aeiou'
    x_1 = x.swapcase()
    lis = []
    for i in list(strl):
        if i in list(x):
            pass
        elif i in list(x_1):
            pass
        else:
            lis.append(i)
    strl = str(lis)
    return strl
print(anti('ASDfghoueXXXEU'))
print '\n'



print '练习八'
print '定义score函数，传一 str 参数,根据词典中字母对应的数值，'
'将每个字母数值相加'
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1,
         "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10,
         "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
def score_1(strl):
    strl = strl.lower()
    lis = list(strl)
    sum = 0
    sum_2 = 0
    for i in lis:
        if i in score.keys():
            sum = sum + score[i]
    return sum
        
print score_1('acbed')
print '\n'

        


print '练习九'
print '定义一个函数，传两个参数，第一个参数中只要包含第二个参数就将相同的项变成*'
def censor(str1,str2):
    low_str1 = str1.lower()
    list_low_str1 = low_str1.split()
    if str2.lower() in list_low_str1:
        num = list_low_str1.count(str2.lower())
        list_str1 = str1.split()
        str_star = len(str2)*'*'
        for i in range(num):
            position = list_low_str1.index(str2.lower())
            list_low_str1[position] = '1'
            list_str1[position] = str_star
        return (' '.join(list_str1))
    else:
        return str1
print (censor('ASD 123 aSD W asd GTJg Asd 1a2b3c','aSd'),censor('asd 456','q'))

def censor(str1,str2):
    str1_low = str1.lower()
    lis_str1_low = str1_low.split()
    lis_str1 = str1.split()
    str2_low = str2.lower()
    lis = []
    star = len(str2) * '*'
    print type(star)
    lenl = range(len(lis_str1_low))
    if str2_low in lis_str1_low:
        for i in lenl:
            word = lis_str1_low[i]
            if word == str2_low:
                lis.append(len(str2) * '*')
            else: 
                lis.append(lis_str1[i])
        return ' '.join(lis)
    else:
        return str1
print (censor('ASD 123 aSD W asd GTJg Asd 1a2b3c','aSd'),censor('asd 456','q'))
print '\n'  



print '练习十 '
print '函数，传两个参数，l为一list，item为任意类型元素；返回l中包含i的个数'
def count_item(lis,item):
    count = 0
    for i in range(len(lis)):
        if lis[i] == item:
            count += 1
    return count
print(count_item([1,2,3,4,2,1,3,1.0,"1"],1))
print(count_item(["b","a","ab","a","","A"], "a"))
print(count_item([["a"],"a"], ["a"]),count_item([["a"],"a"], ["a "])) 
print '\n'



x = '练习十一'
y = x.decode('utf_8')
z = y.encode('gbk')  
print z
print '定义 purify 函数，传一 list 参数；去除该 list 中所有的奇数'
def purify(lis):
    new_lis = []
    l = range(len(lis))
    for i in l:
        if lis[i] % 2 == 0:
            new_lis.append(lis[i])
        else:
            pass
    return new_lis
print purify([1,2,3,4,5,6,7,8,9])
# 注意returned的位置
def purify(lis):
    new_lis = []
    for i in lis:
        if (i % 2 == 0):
            new_lis.append(i)
    return new_lis
print purify([1,2,3,4,5,6,7,8,9])
print '\n'



x = '练习十二'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '传可变参数，该参数全为float，返回所有可变参数相乘的积，无参数则返回 None'
def multiple(*num):
    sun = 1
    if num == ():
        return None
    else:
        for i in (num):
            sun = sun * i
        return float(sun)
print multiple(1,2,3,4),multiple(1.5,2,0),multiple()
print '\n'

    
x = '练习十三'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '定义一个函数，传一个list参数，删除里面重复的项'
def remove_duplicate(lis):
    new_lis = []
    for i in lis:
        if i in new_lis:
            pass
        else:
            new_lis.append(i)
    return new_lis
print remove_duplicate([1,2,3,1,1,2,2,3])
print '\n'




x = '练习十四'
y = x.decode('utf-8')
z = y.encode('gbk')
print z
print '定义一个函数，传一个list参数，如果list的长度为奇数，返回中间数字，'
'偶数，返回中间数字的平均数'
def median(lis):
    l = len(lis)
    if (l % 2 == 0):
        num1 = float(lis[l/2])
        num2 = float(lis[(l/2)-1])
        num = float((num1 + num2)/2)
        return num
    else:
        num = float(lis[(l-1)/2])
        return num
print median([1,2,3]),median([1,2,5,4])
    

