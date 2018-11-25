#!/bin/python

#定义手机号中的号码元素
ele = [ 1, 4 ,0 ,5, 3, 8 ]

#定义上面元素的索引角标
index = [ 0, 3, 5, 2, 0, 4, 1, 3, 3, 5, 0]

tel_list = []
for i in index:
    tel_list.append(ele[i])

tel = ""
for i in tel_list:
    tel += str(i)   #字符串加法
print "Tel: ",tel
