from rest_framework import viewsets
from login_api.serializers import UserLoginSerializer
from login_api.models import User

# Create your views here.
class UserLoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
