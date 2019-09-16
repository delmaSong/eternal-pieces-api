from rest_framework import serializers
from rest_framework.parsers import JSONParser


from join_api.models import Join_tattist

class JoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Join_tattist #모델 설정
        fields = ('tatt_time', 'tatt_id', 'tatt_date', 'tatt_work', 'tatt_addr', 'tatt_intro', 'tatt_profile')  #필드 설정
