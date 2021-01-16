from rest_framework import serializers
from competitions.models import Competition

class CompetitionListSerializer(serializers.ModelSerializer):
    host_nickname = serializers.ReadOnlyField(source='host.nickname')
    
    class Meta:
        model = Competition
        fields = ('id', 'host_nickname', 'host', 'comp_type', 'location', 'category', 'title', 'created_at', 'ended_at', 'max_people', 'joined_people', 'require_money', 'total_money')

class CompetitionJoinSerializer(serializers.ModelSerializer):
    user_pk = serializers.IntegerField(required=True)
    class Meta:
        model = Competition
        fields = ('user_pk', 'total_money')