import csv
import pandas as pd


# def get_ranking_data():
#     f = open('지역별_체력통계_데이터.csv', 'r', encoding='utf-8')
#     rdr = csv.reader(f)
#     for line in rdr:
#         print(line)
#     f.close()

df1 = pd.read_csv("지역별_체력통계_데이터.csv", encoding='utf-8')
a = df1[["CENTER_SD_NM", "CERT_GBN_GOLD", "CERT_GBN_SILVER", "CERT_GBN_BRONZE"]]

print(a)
