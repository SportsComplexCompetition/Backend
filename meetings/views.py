from accounts.models import User
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from meetings.serializers import MeetingListSerializer, CommentListSerializer
from meetings.models import Comment, Meeting
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class MeetingListViewSet(ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Meeting.objects.all()
    serializer_class = MeetingListSerializer

class CommentListViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

class GetEachCommentView(APIView):
    permission_classes = (AllowAny, )
    def get_object(self, meetid):
        return get_object_or_404(Meeting, pk=meetid)

    def get(self, request, meetid):
        meet = self.get_object(meetid)
        data = meet.comment_from_meeting.values()
        for i in data:
            email = User.objects.get(pk=i['user_id']).email
            i['user_email'] = email
        return Response(data=data)