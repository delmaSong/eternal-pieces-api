from django.http import Http404
from rest_framework import status, permissions
from rest_framework import mixins, generics
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FormParser
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import DesignSerializer
from .models import Design

class DesignCreate(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    queryset = Design.objects.all()
    serializer_class = DesignSerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = DesignSerializer(queryset, many=True)
        # return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DesignDetail(APIView):

    def get_object(self, pk):
        try:
            return Design.objects.get(pk=pk)
        except Design.DoesNotExist:
            raise Http404

    """특정 게시물 조회 /upload-design/{pk}"""
    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = DesignSerializer(queryset)
        return Response(serializer.data)


    """특정 게시물 수정 /upload-deisgn/{pk}"""
    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = DesignSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # print(serializer)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
