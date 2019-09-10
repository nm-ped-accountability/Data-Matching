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

# read csv file-- unicode errors used unicode_escape
df = pd.read_csv('StID_Mismatch_NeedToReview.csv',header=0, low_memory=False, encoding = 'unicode_escape')
df_FC_Matched = pd.read_csv('df_FC_MATCHED.csv',header=0, low_memory=False, encoding = 'unicode_escape')
df_Migrant = pd.read_csv('df_Migrant.csv',header=0, low_memory=False, encoding = 'unicode_escape')
df_Program = pd.read_csv('df_Program.csv',header=0, low_memory=False, encoding = 'unicode_escape')
df_120 = pd.read_csv('df_STUDENT_120.csv',header=0, low_memory=False, encoding = 'unicode_escape')
df_19 = pd.read_csv('df_Student_2019.csv',header=0, low_memory=False, encoding = 'unicode_escape')
df_1118 = pd.read_csv('df_Student_11-18.csv',header=0, low_memory=False, encoding = 'unicode_escape')



#print(df_120.info() )

df_Program = df_Program.loc[df_Program['SCHOOL_YEAR'] == '2019-06-30']
df_Program = df_Program[['STUDENT_KEY','PROGRAMS_CODE']]

df_Migrant['Migrant_Tbl'] = 1
df_Migrant = df_Migrant[['SSID','Migrant_Tbl']]

df_FC_Matched['FC_Table'] = 1
df_FC_Matched = df_FC_Matched[['Student ID','FC_Table']]

df_120 = df_120.astype({'STUDENT_KEY':str})
df_120 = df_120[['STUDENT_KEY','STUDENT_ID','STUDENT_GENDER','ETHNIC_DESC','ECONOMIC_CODE','POVERTY_CODE','SPECIAL_ED_CODE','PLAN_504','IMMIGRANT_IND','ENG_PROF_CODE','ENG_PROFICIENCY','MILITARY_FAMILY_DESC','HISPANIC_IND','HOMELESS']]




df_120 = df_120.astype({'STUDENT_ID':str})
df_FC_Matched = df_FC_Matched.astype({'Student ID':str})
df_Program = df_Program.astype({'STUDENT_KEY':str})
df_Migrant = df_Migrant.astype({'SSID':str})
df = df.astype({'S_STUDENT_ID':str})
df_Migrant.rename(columns={'SSID':'S_STUDENT_ID'}, inplace=True)
df_FC_Matched.rename(columns={'Student ID':'S_STUDENT_ID'}, inplace=True)
df_120.rename(columns={'STUDENT_ID':'S_STUDENT_ID'}, inplace=True)
df_19.rename(columns={'STUDENT_ID':'S_STUDENT_ID'}, inplace=True)
df_19 = df_19.astype({'S_STUDENT_ID':str})

df_Program['Count'] = 1

df_Program = df_Program.pivot_table(index='STUDENT_KEY' , columns='PROGRAMS_CODE', values='Count',
                    aggfunc ='sum', margins=True, dropna=True, fill_value=0)
df_Program = df_Program.reset_index()
df_Program = df_Program[['STUDENT_KEY','BEP','T1A','T3']]

data_frames = [df,df_120]

#merge dataframe
df_merged = reduce(lambda left,right: pd.merge(left,right,on=['S_STUDENT_ID'], how='outer'), data_frames)

df_merged = df_merged.dropna(subset = ['STID'])
df_merged = df_merged.reset_index()

data_framesII = [df_merged,df_Program]

#merge dataframe
df_mergedII = reduce(lambda left,right: pd.merge(left,right,on=['STUDENT_KEY'], how='outer'), data_framesII)

df_mergedII = df_mergedII.dropna(subset = ['STID'])
df_mergedII = df_mergedII.reset_index()

data_framesIII = [df_mergedII,df_FC_Matched]
#merge dataframe
df_mergedIII = reduce(lambda left,right: pd.merge(left,right,on=['S_STUDENT_ID'], how='outer'), data_framesIII)

df_mergedIII = df_mergedIII.dropna(subset = ['STID'])
#df_mergedIII = df_mergedIII.reset_index()

data_framesIV = [df_mergedIII,df_Migrant]
#merge dataframe
df_mergedIV = reduce(lambda left,right: pd.merge(left,right,on=['S_STUDENT_ID'], how='outer'), data_framesIV)

df_mergedIV = df_mergedIV.dropna(subset = ['STID'])

data_framesV = [df_mergedIV,df_19]

#merge dataframe
df_mergedV = reduce(lambda left,right: pd.merge(left,right,on=['S_STUDENT_ID'], how='outer'), data_framesV)



df_mergedV = df_mergedV.dropna(subset = ['STID'])


df_1118.rename(columns={'STUDENT_ID':'S_STUDENT_ID'}, inplace=True)
df_1118 = df_1118.astype({'S_STUDENT_ID':str})


data_framesVI = [df_mergedV,df_1118]

#merge dataframe
df_mergedVI = reduce(lambda left,right: pd.merge(left,right,on=['S_STUDENT_ID'], how='outer'), data_framesVI)

df_mergedVI['S_NEW_ARRIVAL'] = str

df_mergedVI.loc[df_mergedVI['STUDENT_KEY'].isnull(), 'S_NEW_ARRIVAL'] = 'Y'

df_mergedVI = df_mergedVI.dropna(subset = ['STID'])

df_mergedVI.to_csv("df_DAD_DemoI.csv", sep=',', encoding='utf-8', index = False)











