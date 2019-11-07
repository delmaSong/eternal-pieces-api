from django.http import Http404
from rest_framework import status
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters import rest_framework as filters
from django.db.models import Q


from .models import Likes
from .serializers import LikesSerializer

class LikesCreate(mixins.ListModelMixin, mixins.CreateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    """좋아요 조회 및 create"""
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

    def get(self, request, *args, **kwargs):
        """모든 좋아요 목록 불러오기"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """좋아요 create"""
        return self.create(request, *args, **kwargs)


    def get_queryset(self):
        """user filtering"""
        queryset = Likes.objects.all()
        user = self.request.query_params.get('user', '')
        like_design = self.request.query_params.get('like_design', '')
        like_tattist = self.request.query_params.get('like_tattist', '')

        if user:    #user id로 조회
            queryset = queryset.filter(user__exact=user)
        if like_design: #user id와 like_design id로 조회시 곧바로 삭제
            queryset = queryset.filter(like_design__exact=like_design)
            queryset.delete()
        elif like_tattist:
            queryset = queryset.filter(like_tattist__exact=like_tattist)
            queryset.delete()

        return queryset


class LikesDetail(APIView):
    """특정 좋아요 RUD"""
    def get_object(self, pk):
        try:
            return Likes.objects.get(pk=pk)
        except Likes.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """특정 좋아요 조회 /likes/{pk}"""
        queryset = self.get_object(pk)
        serializer = LikesSerializer(queryset)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        """특정 좋아요 삭제 /likes/{pk}"""
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
