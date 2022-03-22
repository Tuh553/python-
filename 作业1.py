# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 11:31:29 2022

@author: 24879
"""
#列表遍历
list = ['zhangsan', 'lisi', 'wanger', 'mazi']
for i in range(len(list)):
    print (list[i])
    
#字典遍历
s={'a':1,"b":2,"c":3}
for x in s:
    print (x,s[x])

#存储，查询学生姓名
lst=[]
while True:
    name=input("请输入学生的姓名：")
    if name == "":
        break
    if name in lst:
        print("姓名已存在")
    else:
        lst.append(name)
a=0
check=input("请输入需要查询的姓名:")
for x in range(len(lst)):
    if check==lst[x]:
        print("姓名已存在")
        a=1
        break
if a==0:
    print("姓名不存在")
    
#查询身高
dict={"zhangsan":194,"lisi":178,"wangwu":180}
a=input("请输入需要查询的同学姓名：")
for x in dict:
    if dict[x]>dict[a]:
     print(x,dict[x])
