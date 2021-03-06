
from django.http import Http404
from rest_framework import status, permissions
from rest_framework import mixins, generics
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FormParser
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

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

    def get_queryset(self):
        """필터링 기능"""
        queryset = Join_tattist.objects.all()
        tatt_id = self.request.query_params.get('tatt_id', '')
        area = self.request.query_params.get('area', '')
        if tatt_id:
            queryset = queryset.filter(tatt_id__exact=tatt_id)
        elif area:
            queryset = queryset.filter(tatt_addr__contains=area)
        return queryset

class UserDetail(APIView):

    def get_object(self, pk):
        try:
            return Join_tattist.objects.get(pk=pk)
        except Join_tattist.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """특정 타티스트 조회 /join_api/{pk}"""
        queryset = self.get_object(pk)
        serializer = JoinSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """특정 타티스트 정보 수정 /join_api/{pk}"""
        queryset = self.get_object(pk)
        serializer = JoinSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
