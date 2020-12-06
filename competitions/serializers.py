from rest_framework import serializers
from competitions.models import Competition

class CompetitionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'

class CompetitionJoinSerializer(serializers.ModelSerializer):
    user_pk = serializers.IntegerField(required=True)
    class Meta:
        model = Competition
        fields = ('user_pk', 'money')