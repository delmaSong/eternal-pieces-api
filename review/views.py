from django.http import Http404
from rest_framework import status, permissions
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ReviewSerializer
from .models import Review

class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        """review filtering"""
        queryset = Review.objects.all()
        rv_tatt = self.request.query_params.get('rv_tatt', '')
        if rv_tatt:
            queryset = queryset.filter(rv_tatt__exact=rv_tatt)
        return queryset

class ReviewDetail(APIView):
    """특정 게시물 RUD"""
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """특정 리뷰 조회 /review/{pk}"""
        queryset = self.get_object(pk)
        serializer = ReviewSerializer(queryset)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        """특정 리뷰 수정 /review/{pk}"""
        queryset = self.get_object(pk)
        serializer = ReviewSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        """특정 리뷰 삭제 /review/{pk}"""
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
