from django.shortcuts import render
from rest_framework import mixins, generics, viewsets

from .serializers import BookingSerializer
from .models import Booking

# Create your views here.
class BookingCreate(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """예약 게시물 조회 및 생성"""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get(self, request, *args, **kwargs):
        """모든 예약 목록 불러오기"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """예약 create"""
        return self.create(request, *args, **kwargs)
