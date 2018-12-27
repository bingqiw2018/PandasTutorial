#coding=utf-8 
'''
Created on 2018年3月28日

@author: bingqiw
'''
import pandas as pd
import numpy as np
import sys
import datetime

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data_src = pd.read_excel('d:/tmp/test2018-03-28_13.26.03.xlsx',header=None,encoding='utf-8')
# print data_src.shape
# print data_src.head(1)
data = data_src.loc[:,[1,6,7]]
target = data_src.loc[:,8]
# print data.shape
# print target.shape
X_train, X_test, y_train, y_test = train_test_split(
    data, target, test_size=0.30, random_state=0)
# print X_train;
# print y_train;
 
cls = LogisticRegression()
cls.fit(X_train, y_train)

train_score = cls.score(X_train, y_train)

test_score = cls.score(X_test,y_test)

pre_score = cls.predict(X_test)

# 预测数据导出
df = pd.DataFrame(X_test)
df[9] = pre_score

print df.head()
print df.shape
df = df.loc[df[9] == 1]
print df.shape

print "-----------------------"
sum_score = df.groupby(by=[7])[9].sum()
sum_score = pd.DataFrame(sum_score).sort_values(by=9 ,ascending=False) 
print sum_score
# name = 'd:/tmp/pred'+datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')+'.xlsx'
# sum_score.to_excel(name)
# print('train_score:{0:.2f}; test_score:{1:.2f};'.format(train_score,test_score)) 