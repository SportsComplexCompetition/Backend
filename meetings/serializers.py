from rest_framework import serializers
from meetings.models import Meeting, Comment

class MeetingListSerializer(serializers.ModelSerializer):
    host_nickname = serializers.ReadOnlyField(source='host.nickname')
    class Meta:
        model = Meeting
        fields = ('pk', 'host_nickname', 'host', 'location', 'category', 'title', 'find_people', 'body', 'created_at', 'address')

class CommentListSerializer(serializers.ModelSerializer):
    user_nickname = serializers.ReadOnlyField(source='user.nickname')
    class Meta:
        model = Comment
        fields = ('user_nickname', 'user', 'meeting', 'content', 'created_at')