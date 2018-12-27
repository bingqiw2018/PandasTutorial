#coding=utf-8 
'''
Created on 2018年3月26日

@author: bingqiw
'''
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

boston = load_boston()

X= boston.data
y = boston.target

# print X.shape
# print y.shape
# print X[0]
# print boston.feature_names

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=3)

import time
from sklearn.linear_model import LinearRegression

model = LinearRegression()

start = time.clock()

model.fit(X_train, y_train)

train_score = model.score(X_train, y_train)

cv_score = model.score(X_test, y_test)

print train_score
print cv_score
