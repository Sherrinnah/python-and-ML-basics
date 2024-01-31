# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 09:56:47 2022

@author: SHERRY
"""

import numpy as np
#speed = [80,90,76,45,107,50,35]
#a = np.mean(speed)
#print(a)

from scipy import stats as st
#b = st.mode(speed)
#print(b)

#c = np.std(speed)
#print(c)

#x = np.random.uniform(0, 5, 100)
#print(x)

import matplotlib.pyplot as plt
#x = np.random.normal(5, 1, 100000)

#plt.hist(x,1000)
#plt.show()
#x = [5,7,8,7,6,5,9,8]
#y =[99,86,54,77,80,90,45,75]
#plt.scatter(x,y)

#x = np.random.uniform(5,1,1000)
#y = np.random.uniform(10,2,1000)
#plt.scatter(x,y)

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,11,86,103,87,94,78,77,85,86]
plt.scatter(x,y)
slope,intercept,r,p,std_err = st.linregress(x,y)
def myfunc(x):
    return slope*x + intercept

map(myfunc, x)
model= list(map(myfunc,x))
plt.plot(x,model)
plt.show()
print(r)#gives 0.1 which is not a good relationship. linear regression shouldn't be used to predict future values of either x or y
k=myfunc(10)
print(k)
