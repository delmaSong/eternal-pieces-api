from django.http import Http404
from django.shortcuts import render
from rest_framework import mixins, generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import WorksSerializer
from .models import Works
# Create your views here.
class WorksCreate(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """작업물 조회 및 생성 """
    queryset = Works.objects.all()
    serializer_class = WorksSerializer

    def get(self, request, *args, **kwargs):
        """모든 작업물 목록 불러오기"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """작업물 create"""
        return self.create(request, *args, **kwargs)
