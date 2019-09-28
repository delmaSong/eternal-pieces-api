
from rest_framework import status, permissions
from rest_framework import mixins, generics
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FormParser
from rest_framework.parsers import JSONParser

from .serializers import JoinSerializer
from .models import Join_tattist


class JoinList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    queryset = Join_tattist.objects.all()
    serializer_class = JoinSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
