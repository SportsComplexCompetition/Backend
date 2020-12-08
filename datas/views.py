from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import os
import csv
import pandas as pd
import operator
from django.http import JsonResponse
from datas.datas import get_average
import json

class GetLocalRankingData(APIView):
    def get(self, request):
        df1 = pd.read_csv("지역별_체력통계_데이터.csv", encoding='utf-8')
        a = df1[["CENTER_SD_NM", "CERT_GBN_GOLD", "CERT_GBN_SILVER", "CERT_GBN_BRONZE"]]

        location_name = []

        for i in a["CENTER_SD_NM"]:
            if i not in location_name:
                location_name.append(i)

        result = {}

        for i, row in a.iterrows():
            if row[0] in result:
                result[row[0]][0] += row[1]
                result[row[0]][1] += row[2]
                result[row[0]][2] += row[3]
            else:
                result[row[0]] = [row[1], row[2], row[3]]

        sresult = sorted(result.items(), reverse=True , key=lambda item:item[1])
        return JsonResponse(sresult, safe=False, json_dumps_params={'ensure_ascii': False})

class GetCategoryAverage(APIView):
    def get(self, request):
        result = get_average()
        print(result)
        json_result = json.dumps(result)
        return JsonResponse(json_result, safe=False, json_dumps_params={'ensure_ascii': False})