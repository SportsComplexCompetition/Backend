from django.urls import path, include
from datas import urls as datas_urls
from datas import views

urlpatterns = [
    path('local-rank/', views.GetLocalRankingData.as_view(), name='get_local_rank'),
    path('average/', views.GetCategoryAverage.as_view(), name='get_average'),
    path('topavglow/', views.GetTopAvgLow.as_view(), name='get_top_avg_low'),
]
