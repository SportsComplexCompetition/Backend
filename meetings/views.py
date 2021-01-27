from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from meetings.serializers import MeetingListSerializer, CommentListSerializer
from meetings.models import Comment, Meeting
from rest_framework.permissions import AllowAny

class MeetingListViewSet(ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingListSerializer

class CommentListViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer