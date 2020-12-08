import csv
import pandas as pd
import operator
import numpy as np
import json

def get_category():
    df1 = pd.read_csv("국민연령별추천운동정보.csv", encoding='utf-8')

    category1 = df1['BMI_IDEX_GRAD'] == '정상'
    value1 = df1[category1]

    category2 = value1['SPORTS_STEP_NM'] == '본운동'
    value2 = value1[category2]

    category3 = value2['SE_ACCTO_RECOMEND_SPORTS_RANK'] == 1
    value3 = value2[category3]
    
    print(value3['RECOMEND_SPORTS_NM'].unique())


def get_each_average(data):
    ave12 = int(data['ITEM_F012'].mean())
    ave19 = int(data['ITEM_F019'].mean())
    ave20 = int(data['ITEM_F020'].mean())
    ave21 = int(data['ITEM_F021'].mean())
    ave22 = int(data['ITEM_F022'].mean())
    result = {"data" : [ave12, ave19, ave20, ave21, ave22]}
    return result

def get_all_average(*args):
    i = 0
    section = ['M19to24', 'M25to29', 'M30to34', 'M35to39', 'M40to44', 'M45to49', 'M50to54', 'M55to59', 'M60to64', 'F19to24', 'F25to29', 'F30to34', 'F35to39', 'F40to44', 'F45to49', 'F50to54', 'F55to59', 'F60to64']
    average = []
    for arg in args:
        average.append(get_each_average(arg))
    
    for j in section:
        average[i][j] = average[i]['data']
        del average[i]['data']
        i += 1
    return average
    
def get_average():
    df = pd.read_csv("체력측정_항목별_측정_데이터.csv", encoding='utf-8')
    newdf=df[['AGE_GBN', 'TEST_AGE', 'CERT_GBN', 'TEST_SEX', 'ITEM_F001', 'ITEM_F002', 'ITEM_F012', 'ITEM_F019', 'ITEM_F020', 'ITEM_F021', 'ITEM_F022']]
    newdf=newdf.fillna(newdf.mean())
    is_adult=newdf['AGE_GBN']=='성인'
    is_adult=newdf[is_adult]
    is_teen=newdf['AGE_GBN']=='유소년'
    is_teen=newdf[is_teen]
    adult_Male=is_adult['TEST_SEX']=='M'
    adult_Male=is_adult[adult_Male]
    adult_Female=is_adult['TEST_SEX']=='F'
    adult_Female=is_adult[adult_Female]
    teen_Male=is_teen['TEST_SEX']=='M'
    teen_Male=is_teen[teen_Male]
    teen_Female=is_teen['TEST_SEX']=='F'
    teen_Female=is_teen[teen_Female]
    # Male
    M19to24=((adult_Male['TEST_AGE']>=19) & (adult_Male['TEST_AGE']<=24))
    M19to24=adult_Male[M19to24]
    M25to29=((adult_Male['TEST_AGE']>=25) & (adult_Male['TEST_AGE']<=29))
    M25to29=adult_Male[M25to29]
    M30to34=((adult_Male['TEST_AGE']>=30) & (adult_Male['TEST_AGE']<=34))
    M30to34=adult_Male[M30to34]
    M35to39=((adult_Male['TEST_AGE']>=35) & (adult_Male['TEST_AGE']<=39))
    M35to39=adult_Male[M35to39]
    M40to44=((adult_Male['TEST_AGE']>=40) & (adult_Male['TEST_AGE']<=44))
    M40to44=adult_Male[M40to44]
    M45to49=((adult_Male['TEST_AGE']>=45) & (adult_Male['TEST_AGE']<=49))
    M45to49=adult_Male[M45to49]
    M50to54=((adult_Male['TEST_AGE']>=50) & (adult_Male['TEST_AGE']<=54))
    M50to54=adult_Male[M50to54]
    M55to59=((adult_Male['TEST_AGE']>=55) & (adult_Male['TEST_AGE']<=59))
    M55to59=adult_Male[M55to59]
    M60to64=((adult_Male['TEST_AGE']>=60) & (adult_Male['TEST_AGE']<=64))
    M60to64=adult_Male[M60to64]
    M65to69=((adult_Male['TEST_AGE']>=65) & (adult_Male['TEST_AGE']<=69))
    M65to69=adult_Male[M65to69]
    M70to74=((adult_Male['TEST_AGE']>=70) & (adult_Male['TEST_AGE']<=74))
    M70to74=adult_Male[M70to74]
    M75to79=((adult_Male['TEST_AGE']>=75) & (adult_Male['TEST_AGE']<=79))
    M75to79=adult_Male[M75to79]
    M80to84=((adult_Male['TEST_AGE']>=80) & (adult_Male['TEST_AGE']<=84))
    M80to84=adult_Male[M80to84]
    M85=adult_Male['TEST_AGE']>=85
    M85=adult_Male[M85]
    # Female
    F19to24=((adult_Female['TEST_AGE']>=19) & (adult_Female['TEST_AGE']<=24))
    F19to24=adult_Female[F19to24]
    F25to29=((adult_Female['TEST_AGE']>=25) & (adult_Female['TEST_AGE']<=29))
    F25to29=adult_Female[F25to29]
    F30to34=((adult_Female['TEST_AGE']>=30) & (adult_Female['TEST_AGE']<=34))
    F30to34=adult_Female[F30to34]
    F35to39=((adult_Female['TEST_AGE']>=35) & (adult_Female['TEST_AGE']<=39))
    F35to39=adult_Female[F35to39]
    F40to44=((adult_Female['TEST_AGE']>=40) & (adult_Female['TEST_AGE']<=44))
    F40to44=adult_Female[F40to44]
    F45to49=((adult_Female['TEST_AGE']>=45) & (adult_Female['TEST_AGE']<=49))
    F45to49=adult_Female[F45to49]
    F50to54=((adult_Female['TEST_AGE']>=50) & (adult_Female['TEST_AGE']<=54))
    F50to54=adult_Female[F50to54]
    F55to59=((adult_Female['TEST_AGE']>=55) & (adult_Female['TEST_AGE']<=59))
    F55to59=adult_Female[F55to59]
    F60to64=((adult_Female['TEST_AGE']>=60) & (adult_Female['TEST_AGE']<=64))
    F60to64=adult_Female[F60to64]
    F65to69=((adult_Female['TEST_AGE']>=65) & (adult_Female['TEST_AGE']<=69))
    F65to69=adult_Female[F65to69]
    F70to74=((adult_Female['TEST_AGE']>=70) & (adult_Female['TEST_AGE']<=74))
    F70to74=adult_Female[F70to74]
    F75to79=((adult_Female['TEST_AGE']>=75) & (adult_Female['TEST_AGE']<=79))
    F75to79=adult_Female[F75to79]
    F80to84=((adult_Female['TEST_AGE']>=80) & (adult_Female['TEST_AGE']<=84))
    F80to84=adult_Female[F80to84]
    F85=adult_Female['TEST_AGE']>=85
    F85=adult_Female[F85]
    result = get_all_average(M19to24, M25to29, M30to34, M35to39, M40to44, M45to49, M50to54, M55to59, M60to64, F19to24, F25to29, F30to34, F35to39, F40to44, F45to49, F50to54, F55to59, F60to64)
    return result
