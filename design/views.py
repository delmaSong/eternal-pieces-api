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
from rest_framework.viewsets import GenericViewSet
from django_filters import rest_framework as filters

from .serializers import DesignSerializer
from .models import Design

class DesignCreate(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """게시물 조회 및 create"""
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    queryset = Design.objects.all()
    serializer_class = DesignSerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = DesignSerializer(queryset, many=True)
        # return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        """모든 도안 목록 불러오기"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """도안 create"""
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        """design_style filtering"""
        queryset = Design.objects.all()
        design_style = self.request.query_params.get('design_style', '')
        tatt_id = self.request.query_params.get('tatt_id', '')
        if design_style:
            queryset = queryset.filter(design_style__exact=design_style)
        elif tatt_id:
            queryset = queryset.filter(tatt_id__exact=tatt_id)
        return queryset


class DesignDetail(APIView):
    """특정 게시물 RUD"""
    def get_object(self, pk):
        try:
            return Design.objects.get(pk=pk)
        except Design.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """특정 게시물 조회 /upload-design/{pk}"""
        queryset = self.get_object(pk)
        serializer = DesignSerializer(queryset)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        """특정 게시물 수정 /upload-deisgn/{pk}"""
        queryset = self.get_object(pk)
        serializer = DesignSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        """특정 게시물 삭제 /upload-design/{pk}"""
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
