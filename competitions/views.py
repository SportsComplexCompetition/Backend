from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from competitions.models import  Competition
from competitions.serializers import CompetitionListSerializer, CompetitionJoinSerializer
from rest_framework import mixins, generics
from accounts.models import User

class CompetitionListViewSet(ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionListSerializer


class CompetitionJoinAPIView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionJoinSerializer

    def put(self, request, pk):
        competition = Competition.objects.get(pk=pk)
        competition.joined_people.add(User.objects.get(pk=request.data['user_pk']))
        now_money = competition.money
        request.data['money'] += now_money
        return self.update(request)

    