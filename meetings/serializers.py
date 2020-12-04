from rest_framework import serializers
from meetings.models import Meeting, Comment

class MeetingListSerializer(serializers.ModelSerializer):
    host_email = serializers.ReadOnlyField(source='host.email')
    class Meta:
        model = Meeting
        fields = ('host_email', 'host', 'location', 'title', 'find_people', 'body', 'created_at')

class CommentListSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Comment
        fields = ('user_email', 'user', 'meeting', 'content', 'created_at')