# Jeanho Rodriguez
# 09.09.2019
# CCR

import pandas as pd
import json
import xlrd
import numpy as np
import os
os.getcwd()
os.listdir(os.getcwd())
from numpy import nan as NA
from pandas import Series, DataFrame
from functools import reduce
from collections import Counter


# how to set display
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)

# increase column width
pd.set_option('display.max_colwidth', 1000)


df = pd.read_csv('df_DAD_DemoII_clean.csv',header=0, low_memory=False, encoding = 'unicode_escape')

# ELL_LEVEl
df.loc[df['S_ELL_LEVEL'] == 1.0, 'S_ELL_STATUS'] = 'Y'
df.loc[df['S_ELL_LEVEL'] != 1.0, 'S_ELL_STATUS'] = 'N'

# BEP_LEVEL
df.loc[df['S_BEP'] == 1.0, 'S_BEP'] = 'Y'
df.loc[df['S_BEP'] == 0.0, 'S_BEP'] = 'N'

# S_POVERTY_CODE
df.loc[df['S_POVERTY_CODE'] == 1.0, 'S_POVERTY'] = 'Y'

# S_TITLE1_LEVEL
df.loc[df['S_TITLE1'] == 1.0, 'S_TITLE1'] = 'Y'
df.loc[df['S_TITLE1'] == 0.0, 'S_TITLE1'] = 'N'

# S_TITLEIII_LEVEL
df.loc[df['S_TITLE_III'] == 1.0, 'S_TITLE_III'] = 'Y'
df.loc[df['S_TITLE_III'] == 0.0, 'S_TITLE_III'] = 'N'

df = df.astype({'S_DOB': str})
df = df.astype({'S_BMONTH': str})

df['S_BMONTH'] = df['S_DOB'].str[4:6]
df['S_BDAY'] = df['S_DOB'].str[6:8]
df['S_BYEAR'] = df['S_DOB'].str[0:4]

df['S_DOB'] = df['S_BMONTH'] + '/' + df['S_BDAY'] + '/' + df['S_BYEAR']


df.to_csv('df_DAD_Demo09102019.csv',sep=',', encoding='utf-8', index = False)







# Map for Eth
#Eth_code_map = {'1':'ALLSTU','2':'FEMALE','3':'MALE','4':'WHITE','5':'BLACK','6':'HISPANIC','7':'ASIAN','8':'NATIVE',
                 #'9':'FRL','10':'SWD','11':'ELL','12':'HOMELESS','13':'MILITARY','14':'FOSTER','15':'MIGRANT'}

#df_soap_merge_final = df_soap_merge_final.astype({'Sort_Code':str})
#df_soap_merge_final = df_soap_merge_final.astype({'Code':str})
#df_soap_merge_final = df_soap_merge_final.astype({'SchoolCode':str})


#df_soap_merge_final['Sort_Code'] = df_soap_merge_final['Sort_Code'].map(sort_code_map) #map function applied with map rule