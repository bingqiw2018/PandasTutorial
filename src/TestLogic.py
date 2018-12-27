#coding=utf-8 
'''
Created on 2018年3月25日

@author: bingqiw
'''
import numpy as np
import matplotlib.pyplot as plt

# 使用交叉验证的方法，把数据集分为训练集合测试集
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

# 加载iris数据集
def load_data():
    diabetes = datasets.load_iris()

    # 将数据集拆分为训练集和测试集 
    X_train, X_test, y_train, y_test = train_test_split(
    diabetes.data, diabetes.target, test_size=0.30, random_state=0)
    return X_train, X_test, y_train, y_test

# 使用LogisticRegression考察线性回归的预测能力
def test_LogisticRegression(X_train, X_test, y_train, y_test):
    # 选择模型
    cls = LogisticRegression()
    print y_train
    # 把数据交给模型训练
    cls.fit(X_train, y_train)

    print("Coefficients:%s, intercept %s"%(cls.coef_,cls.intercept_))
    print("Residual sum of squares: %.2f"% np.mean((cls.predict(X_test) - y_test) ** 2))
    print('Score: %.2f' % cls.score(X_test, y_test))

if __name__=='__main__':
    X_train,X_test,y_train,y_test=load_data() # 产生用于回归问题的数据集
    test_LogisticRegression(X_train,X_test,y_train,y_test) # 调用 test_LinearRegression