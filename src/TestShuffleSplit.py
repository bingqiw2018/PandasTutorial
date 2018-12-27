#coding=utf-8 
'''
Created on 2018年3月29日

@author: bingqiw
'''
from sklearn.model_selection import ShuffleSplit
import numpy as np

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# print X
y = np.array([5, 6, 7, 8])
# print y

rs = ShuffleSplit(n_splits=3, test_size=0.25, random_state=0)
for train_index, test_index in rs.split(X):
    print("TRAIN:", train_index, "TEST:", test_index)
# for train_index, test_index in rs.split(X):
#     print("TRAIN:", X[train_index], "TEST:", X[test_index])
# print "--------------------------------------------------------"    

rs = ShuffleSplit(n_splits=4, test_size=.25,random_state=0)
# for train_index, test_index in rs.split(X):
#     print("TRAIN:", train_index, "TEST:", test_index)
# print "--------------------------------------------------------"    

# for train_index, test_index in rs.split(X,y):
# #     print("TRAIN:", X[train_index], "TEST:", X[test_index])
#     print("TRAIN:", y[train_index], "TEST:", y[test_index])
    