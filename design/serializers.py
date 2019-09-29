from rest_framework import serializers
from design.models import Design

class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design #모델 설정
        fields= '__all__'
