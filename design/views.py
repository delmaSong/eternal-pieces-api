from rest_framework import status, permissions
from rest_framework import mixins, generics
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FormParser
from rest_framework.parsers import JSONParser

from .serializers import DesignSerializer
from .models import Design

class DesignList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    queryset = Design.objects.all()
    serializer_class = DesignSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
