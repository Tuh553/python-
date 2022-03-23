# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 11:24:07 2022
@author: 24879
"""
import numpy as np
names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳','钱易铭'])
subjects=np.array(['Math', 'English', 'Python', 'Chinese', 'Art', 'Database', 'Physics'])
scores= np.array([[70,85,77,90,82,84,89],
[60,64,80,75,80,92,90], [90,93,88,87,86,90,91],
[80,82,91,88,83,86,80],[88,72,78,90,91,73,80]])
#2.1思考题1
print(subjects[[1,2,4]])
print(names[-3])
print(names[2:])
print(subjects[2:4])
print(subjects[(subjects=='English')|(subjects=='Physics')])
#2.1思考题2
print(scores[[0,3]])
print(scores[[2,4]][:,(subjects == 'Math') | (subjects == 'Python')])
print(scores[:,(subjects == 'Math') | (subjects == 'Art')])
print(scores[(names=='王微') | (names=='刘旭阳')][:,(subjects == 'English') | (subjects == 'Art')])
#2.1思考题3
a=np.arange(10,20).reshape(2,5)
print(a)
#2.2思考题1
bonus=np.array([0,-3,0,0,0,0,0])
print(scores+bonus)
#2.2思考题2
print(scores.mean (axis = 1))
#2.2思考题3
a=np.random.uniform(-1,1,size=(3,4))
print(a.sum()) 
#2.3思考题
steps = 100
rndwlk = np.random.randint(0, 2, size = (2,steps))
rndwlk = np.where( rndwlk>0, 1, -1 )
position = rndwlk.cumsum(axis = 1)
dists = np.sqrt(position[0]**2 + position[1]**2)
np.set_printoptions(precision=4)
print(dists)
print(dists())
#运行次数越多，发现平均距离趋近10左右）
#综合题1
import numpy as np
market=np.array(['大润发','沃尔玛','联华','农工商'])
fruit=np.array(['苹果','梨','香蕉','橘子','芒果'])
price=np.random.randint(4,11,size=(4,5))
price[(market=='大润发'),(fruit=='苹果')]+1
price[(market=='联华'),(fruit=='香蕉')]+1
price[(market=='农工商')]-2
print(price[:,(fruit=='苹果')].mean())
print(price[:,(fruit=='芒果')].mean())
print(market[price[:,fruit=='橘子'].argmax()]) 
#综合题2
np.set_printoptions( precision = 4)
rndwlk = np.random.normal (0, 1, size = (3,10))
rndwlk = np.where( rndwlk>0, 1, -1 )
print(rndwlk)
position = rndwlk.cumsum(axis = 1)
print (position)
dists = np.sqrt(position[0]**2 + position[1]**2 + position[2]**2)
print(dists)
z=np.abs(position[2])
print(z.max())
print(dists.min())


