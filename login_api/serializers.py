from rest_framework import serializers

from login_api.models import User

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'user_pw', 'role_tatt')
