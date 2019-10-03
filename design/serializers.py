from rest_framework import serializers
from design.models import Design

class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design #모델 설정
        fields= ('id', 'design_name', 'design_price', 'design_size', 'design_spent_time', 'design_style', 'design_desc', 'tatt_id', 'design_photo' )
