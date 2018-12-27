#coding=utf-8 
'''
Created on 2018年4月20日

@author: bingqiw
'''
import pandas as pd
import MySQLdb as md

prod_con  = md.connect(host='10.191.33.31', port=3306,user='prodqry', passwd='123456', db='prod')
sysman_con = md.connect(host='10.191.33.31', port=3306,user='sysmanqry', passwd='123456', db='sysman')
report_con = md.connect(host='10.191.33.31', port=3306,user='reportqry', passwd='123456', db='report')
param_con = md.connect(host='10.191.33.30', port=3306,user='paramqry', passwd='123456', db='param')
hbase_con =  md.connect(host='10.191.5.227', port=3307,user='root', passwd='Bata@Sale!', db='phoenix')
hbase_con =  md.connect(host='10.191.5.227', port=3307,user='root', passwd='Bata@Sale!', db='phoenix')

df = pd.read_sql('select * from SYS_FTP_CONFIG', con=param_con) 

print df.shape  

prod_con.close()