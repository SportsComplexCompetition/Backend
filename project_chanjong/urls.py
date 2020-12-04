"""project_chanjong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from datas import urls as datas_urls
from meetings import urls as meetings_urls
from accounts import urls as accounts_urls

from rest_framework import routers
from meetings.views import MeetingListViewSet, CommentListViewSet


router = routers.DefaultRouter()
router.register('meetinglist', MeetingListViewSet, basename='meeting')
router.register('commentlist', CommentListViewSet, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('data/', include(datas_urls)),
    path('meeting/', include(meetings_urls)),
    path('accounts/', include(accounts_urls)),

]
