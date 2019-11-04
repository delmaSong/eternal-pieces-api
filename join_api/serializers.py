from rest_framework import serializers
from rest_framework.parsers import JSONParser

from join_api.models import Join_tattist


class JoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Join_tattist #모델 설정
        fields = '__all__'  #필드 설정
