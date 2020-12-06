from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from competitions.models import  Competition
from competitions.serializers import CompetitionListSerializer

class CompetitionListViewSet(ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionListSerializer