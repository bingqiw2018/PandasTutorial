#coding=utf-8 
'''
Created on 2018年4月25日

@author: bingqiw
'''

import pandas as pd
import numpy as np

# python 数组演示
arr_py_01 = []
arr_py_01.append([1,2])
arr_py_01.append([3,4])
arr_py_01.append([5,6])
arr_py_02 = arr_py_01.pop()
print arr_py_01
print arr_py_02
print "---------------------"

print "numpy 数组演示"
arr_np_01 = np.array([]) #可以定义，arr_np_01没有可用的接口
arr_np_02 = np.array([1,2])
print arr_np_02

arr_np_03 = np.ones((3,5)) #
print arr_np_03
# array([[ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.]])
arr_np_04 = np.random.randn(15).reshape(arr_np_03.shape)
print arr_np_04
# array([[-0.09666833,  1.47064828, -1.94608976,  0.2651279 , -0.32894787],
#        [ 1.01187699,  0.39171167,  1.49607091,  0.79216196,  0.33246644],
#        [ 1.71266238,  0.86650837,  0.77830394, -0.90519422,  1.55410056]])

arr_np_05 = np.concatenate([arr_np_03,arr_np_04],axis=0) #在纵轴上合并
print "-------------------------------"
print arr_np_05
# array([[ 1.        ,  1.        ,  1.        ,  1.        ,  1.        ],
#        [ 1.        ,  1.        ,  1.        ,  1.        ,  1.        ],
#        [ 1.        ,  1.        ,  1.        ,  1.        ,  1.        ],
#        [-0.09666833,  1.47064828, -1.94608976,  0.2651279 , -0.32894787],
#        [ 1.01187699,  0.39171167,  1.49607091,  0.79216196,  0.33246644],
#        [ 1.71266238,  0.86650837,  0.77830394, -0.90519422,  1.55410056]])
arr_np_06 = np.concatenate([arr_np_03,arr_np_04],axis=1) #在横轴上合并
print "-------------------------------"
print arr_np_06
# [[ 1.          1.          1.          1.          1.         -0.78836937   -0.34213923  1.00797184  1.93350189  1.2489456 ]
#  [ 1.          1.          1.          1.          1.          2.17558495    0.89545936  0.80965176 -3.35800094  0.26032089]
#  [ 1.          1.          1.          1.          1.         -0.68032844    0.32732112 -0.06297042 -0.68971893 -0.34420997]]

arr_np_05 = np.hstack([arr_np_03,arr_np_04]) # 水平 horizon 
arr_np_06 = np.vstack([arr_np_03,arr_np_04]) # 垂直 vertical 
print "hstack-------------------------------"
print arr_np_05
print arr_np_06

print "pandas数组演示"
from pandas import DataFrame
frame1=DataFrame([[1,2,3],[4,5,6]])
frame2=DataFrame([[7,8,9],[10,11,12]])
frame3 = pd.concat([frame1,frame2],axis=0,ignore_index=True) # 合并的数组是一个可迭代的列表。
print frame3
#     0   1   2
# 0   1   2   3
# 1   4   5   6
# 0   7   8   9
# 1  10  11  12


frame4 = pd.concat([frame1,frame2],axis=1,ignore_index=True)
print frame4
#    0  1  2   3   4   5
# 0  1  2  3   7   8   9
# 1  4  5  6  10  11  12
