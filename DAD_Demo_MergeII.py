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


df = pd.read_csv('df_DAD_DemoI.csv',header=0, low_memory=False, encoding = 'unicode_escape')





df['S_BMONTH'] = str
df['S_BDAY'] = str
df['S_BYEAR'] =str
df['STATUS'] = str
df['S_SCHNUMB'] = str
df['check_StID'] = str
df['S_STUDENT_IDII']=str
df['S_STUDENTNAME'] =str

df = df[['Case_ID','STID','S_STUDENT_ID','S_STUDENT_IDII','DISTRICT_CODE','DISTRICT_NAME','LOCATION_ID','LOCATION_NAME',
                         'STUDENT_LAST_NM','STUDENT_FIRST_NM','STUDENT_MID_INIT','STUDENT_NAME','DOB','S_BMONTH',
                         'S_BDAY','S_BYEAR','STUDENT_GENDER_y','ETHNIC_DESC_y','CURR_GRADE_LVL','SPECIAL_ED_CODE_y',
                         'Migrant_Tbl','ENG_PROFICIENCY_y','HISPANIC_IND_y','ECONOMIC_CODE_y','POVERTY_CODE_y','S_STUDENTNAME','BEP','T1A',
                         'MILITARY_FAMILY_DESC_y','GIFTED_TALENTED','PLAN_504_y','ENG_PROF_CODE_y','IMMIGRANT_IND_y',
                         'S_NEW_ARRIVAL','T3','FC_Table','HOMELESS_y','STATUS','TestbookID','Vendor_SchNumb',
                         'Vendor_DistCode','Vendor_DistName','Vendor_SchCode','Vendor_SchName','Tested_Grade',
                         'Tested_Grade_Listen','Tested_Grade_Read','Tested_Grade_Speak','Tested_Grade_Write','STARS_Grade',
                         'Pref_Grade','Accomm','CBT','CBT_Listen','CBT_Read','CBT_Speak','CBT_Write','Testname','Subtest',
                         'TestCode','TestLang','PL','PL_Listen','PL_Read','PL_Speak','PL_Write','PL_Comprehension','PL_Oral',
                         'PL_Literacy','Proficient','SS','NewSS','SS_Listen','SS_Read','SS_Speak','SS_Write','SS_Comprehension',
                         'SS_Oral','SS_Literacy','IstationTime','Pearson_SGP','Accty_StID','Accty_Lname','Accty_Fname',
                         'Accty_MI','S_SCHNUMB','check_StID']]

df.rename(columns={'S_STUDENT_ID':'STARS_STUDENT_ID'}, inplace=True)
df.rename(columns={'S_STUDENT_IDII':'S_STUDENT_ID'}, inplace=True)
df.rename(columns={'DISTRICT_CODE':'S_DISTRICT_CODE'}, inplace=True)
df.rename(columns={'DISTRICT_NAME':'S_DISTRICT_NAME'}, inplace=True)
df.rename(columns={'LOCATION_ID':'S_LOCATION_CODE'}, inplace=True)
df.rename(columns={'LOCATION_NAME':'S_LOCATION_NAME'}, inplace=True)
df.rename(columns={'STUDENT_LAST_NM':'S_LASTNAME'}, inplace=True)
df.rename(columns={'STUDENT_FIRST_NAME':'S_FIRSTNAME'}, inplace=True)
df.rename(columns={'STUDENT_MID_INIT':'S_MIDDLE_NAME'}, inplace=True)
df.rename(columns={'STUDENT_NAME':'S_STUDENT_NAME'}, inplace=True)
df.rename(columns={'DOB':'S_DOB'}, inplace=True)
df.rename(columns={'STUDENT_GENDER_y':'S_GENDER'}, inplace=True)
df.rename(columns={'ETHNIC_DESC_y':'S_ETNICITY'}, inplace=True)
df.rename(columns={'CURR_GRADE_LVL':'S_GRADE'}, inplace=True)
df.rename(columns={'SPECIAL_ED_CODE_y':'S_SPECIAL_ED'}, inplace=True)
df.rename(columns={'Migrant_Tbl':'S_MIGRANT'}, inplace=True)
df.rename(columns={'ENG_PROFICIENCY_y':'S_ELL_STATUS'}, inplace=True)
df.rename(columns={'HISPANIC_IND_y':'S_HISPANIC_INDICATOR'}, inplace=True)
df.rename(columns={'ECONOMIC_CODE_y':'S_FRLP'}, inplace=True)
df.rename(columns={'POVERTY_CODE_y':'S_POVERTY_CODE'}, inplace=True)
df.rename(columns={'BEP':'S_BEP'}, inplace=True)
df.rename(columns={'T1A':'S_TITLE1'}, inplace=True)
df.rename(columns={'MILITARY_FAMILY_DESC_y':'S_MILITARY'}, inplace=True)
df.rename(columns={'GIFTED_TALENTED':'S_GIFTED'}, inplace=True)
df.rename(columns={'PLAN_504_y':'S_PLAN504'}, inplace=True)
df.rename(columns={'ENG_PROF_CODE_y':'S_ELL_LEVEL'}, inplace=True)
df.rename(columns={'IMMIGRANT_IND_y':'S_IMMIGRANT'}, inplace=True)
df.rename(columns={'T3':'S_TITLE_III'}, inplace=True)
df.rename(columns={'FC_Table':'S_FOSTER'}, inplace=True)
df.rename(columns={'HOMELESS_y':'S_HOMELESS'}, inplace=True)



#df.drop_duplicates(keep=False, inplace=True)

#df.to_csv('df_DAD_DemoII.csv',sep=',', encoding='utf-8', index = False)

