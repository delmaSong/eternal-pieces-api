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

    def get_queryset(self):
        """타티스트 아이디로 필터링"""
        queryset = Booking.objects.all()
        book_tatt = self.request.query_params.get('book_tatt', '')
        if book_tatt:
            queryset = queryset.filter(book_tatt__exact=book_tatt)
        return queryset

    def get_booker(self):
        """예약자 아이디로 필터링"""
        queryset = Booking.objects.all()
        booker = self.request.query_params.get('booker', '')
        if booker:
            queryset = queryset.filter(booker__exact=booker)
        return queryset
