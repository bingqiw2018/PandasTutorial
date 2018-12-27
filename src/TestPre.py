#coding=utf-8 
'''
Created on 2018年3月21日

@author: bingqiw
'''
import pandas as pd
import numpy as np
import datetime

data = pd.read_excel('d:/tmp/test2018-03-25_12.18.10.xlsx',header=None,encoding='utf-8')
# print data.head(5)

df = pd.DataFrame(data,
                  columns = [6,7,8]
                  )
print df.head(3)

dataMat = df.iloc[0:3,[0,1]]
print dataMat

classLabel = df.iloc[0:3,[2]]
print classLabel

alpha = 0.001

maxCycles = 10

# 定义sigmoid函数
def sigmoid(x):
    y = 1.0/(1 + np.exp(-x))
    return y

def gradAscent(dataMat, classLabel, alpha, maxCycles):
    
    dataMatrix = np.mat(dataMat) # 数据dataMat是数组类型
    print dataMatrix
    labelMatrix = np.mat(classLabel).transpose() # 数据classLabel是数组类型，且做矩阵转置
    print labelMatrix
    
    m, n = np.shape(dataMatrix)
    print m,n
    weights = np.ones((n,1),int) #获取维度(n,1)的单位矩阵
    print weights
#     循环迭代
    for i in range(maxCycles):
        h = sigmoid(dataMatrix * weights)
        error = (labelMatrix - h)
        weights = weights + alpha * dataMatrix.transpose() * error
    
    return weights

print gradAscent(dataMat, classLabel, alpha, maxCycles)

