
#coding=utf-8 
'''
Created on 2018年3月17日

@author: bingqiw
'''
import pandas as pd
import sys
import datetime

# 导出文件的设置，系统字符集
reload(sys)
sys.setdefaultencoding('utf-8')
# print(sys.getdefaultencoding())

# pandas导入文件，通过read_table方法
data = pd.read_table('d:/tmp/sync_sale_order_info_new.txt',header=None,encoding='utf-8')
print('数据录入完毕')
print(data.shape)
# 根据数据data构建DataFrame数据结构，data.head(1)表示取记录第1条记录，空记录以0来填充
df = pd.DataFrame(data.fillna(0))
print('数据空值处理')
print(df.shape)
# 改变列名称
df.columns = ['TRADE_TYPE','ACTIVE_TYPE','SUBSCRIBE_ID','SOURCE_SYSTEM','PROV_ID','PROV_NAME','AREA_ID','AREA_NAME','CITY_CODE','CITY_NAME','CHANNEL_CODE','CHANNEL_NAME','STAFF_ID','UPDATE_TIME','OLD_SUBSCRIBE_ID','PROPERTY_CODE','PROPERTY_DESC','NEW_PROPERTY_CODE','NEW_PROPERTY_DESC','SALE_PRICE','IMEI','NEW_TERMINAL_ID','OLD_TERMINAL_ID','SERVICE_NMUBER','RECOMMEND_NAME','RECOMMEND_NUMBER','RECOMMEND_ID','DATA_SOURCE','SYNC_FILE_NAME','SYNC_DATE','COMM_TYPE','SETTLEMENT_PRICE','COMM_ID']
print('修改列名称')
print(df.shape)
# 过滤行
data = df.loc[(df['PROV_ID'] == 17) & 
              (df['TRADE_TYPE'] != 0) & 
              (df['SALE_PRICE'] != 0) & 
              (df['UPDATE_TIME'] != 0)
              ] 
print('过滤行数据，得到苏州数据')
print(data.shape)
# 过滤列
df = pd.DataFrame(data,
                  columns = ['SUBSCRIBE_ID','TRADE_TYPE','PROV_ID','PROV_NAME','STAFF_ID','UPDATE_TIME','SALE_PRICE']
                  ).head(1000)
# df['isHotScore'] = [True,True,True,True,True]
print('过滤列数据，取前1000条数据')
print(df.shape)
print(df.head(1))

def func_is_hot_score(price):
    if price >100000:
        return 1
    else:
        return 0
def func_to_one(update_time):
    if update_time:
        time = int(update_time.split(' ')[1].split(':')[0])
        return time
    else:
        return 0  
    
df['isHotScore'] = df.apply(lambda x: func_is_hot_score(x.SALE_PRICE),axis=1)
df['UPDATE_TIME_NEW'] = df.apply(lambda x: func_to_one(x.UPDATE_TIME),axis=1)
print('汇总新列isHotScore数据')
print(df.shape)  
print(df.head(1))  

name = 'd:/tmp/test'+datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')+'.xlsx'
df.to_excel(name,index=False)
print('end')