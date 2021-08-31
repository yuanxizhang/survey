from rest_framework import serializers
from .models import Survey


class SurveySerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Survey
        fields = ('id', 'author', 'title', 'last_udpated_on', 'is_active')