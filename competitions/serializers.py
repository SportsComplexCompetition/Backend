from rest_framework import serializers
from competitions.models import Competition

class CompetitionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'