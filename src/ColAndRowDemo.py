#coding=utf-8 
'''
Created on 2018年3月17日
@author: bingqiw
'''
import pandas as pd
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

data = pd.read_excel('d:/tmp/test.xlsx')
print(data.shape)
df = pd.DataFrame(data)

print('starting')
data2 = df.loc[df['PROV_NAME'] != '江苏'] 
print(data2.shape)
df2 = pd.DataFrame(data2)   
data3 = df2[['SUBSCRIBE_ID','TRADE_TYPE','PROV_ID','PROV_NAME','STAFF_ID','UPDATE_TIME','SALE_PRICE']]
print(data3.shape)
print(data3.head())
print('end')