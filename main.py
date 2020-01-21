import os, pandas as pd

df1 = pd.DataFrame(pd.read_excel('2019年信贷人员上岗资格考试_各省分行成绩.xlsx'))
df2 = pd.DataFrame(pd.read_excel('中国农业发展银行2019年信贷专业持证上岗资格考试（成绩表）(1).xlsx'))
df3 = pd.DataFrame(pd.read_excel('全行人员20191231.xls'))

df4=pd.merge(df3,df2,how='left',left_on='人员固定编号',right_on='人员固定编号')

print(df1.head())
print(df2.head())
print(df3.head())

 
