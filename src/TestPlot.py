#coding=utf-8 
'''
Created on 2018年3月28日

@author: bingqiw
'''
from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(- np.pi, np.pi, 200)
print x.shape

C,S = np.cos(x),np.sin(x)
print C.shape
print S.shape

plt.plot(x,C, color="blue" , linewidth=2.0, linestyle="-")
plt.plot(x,S, color="red", linewidth=2.0, linestyle="-")

plt.xlim(x.min()*1.1, x.max()*1.1)
plt.grid()

# plt.show()

