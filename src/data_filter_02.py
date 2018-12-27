
#coding=utf-8 
'''
Created on 2018年3月17日

@author: bingqiw
'''
import pandas as pd

# pandas导入文件，通过read_table方法
data = pd.read_table('D:/Program Files/eclipse4.6/workspace/PandasDemo/data/sync_sale_order_info_new.txt',header=None,encoding='utf-8')
print(data.head())
print('end')