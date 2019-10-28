from rest_framework import serializers
from works.models import Works

class WorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = '__all__'
