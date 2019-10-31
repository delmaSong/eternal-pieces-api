from django.http import Http404
from django.shortcuts import render
from rest_framework import mixins, generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

    def get_queryset(self):
        """작업물 필터링"""
        queryset = Works.objects.all()
        tatt_id = self.request.query_params.get('tatt_id', '')
        if tatt_id:
            queryset = queryset.filter(tatt_id__exact=tatt_id)
        return queryset
class WorksDetail(APIView):

    def get_object(self, pk):
        try:
            return Works.objects.get(pk=pk)
        except Works.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """특정 작업물 조회 /works/{pk}"""
        queryset = self.get_object(pk)
        serializer = WorksSerializer(queryset)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        """특정 작업물 삭제 /works/{pk}"""
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
