import csv
import pandas as pd
import operator

df1 = pd.read_csv("체력측정_항목별_측정_데이터.csv", encoding='utf-8')
print(df1['CENTER_NM'].value_counts())