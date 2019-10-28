from django.http import Http404
from django.shortcuts import render
from rest_framework import mixins, generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

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
        booker = self.request.query_params.get('booker', '')
        if book_tatt:
            queryset = queryset.filter(book_tatt__exact=book_tatt)
        elif booker:
            queryset = queryset.filter(booker__exact=booker)
        return queryset

class BookingDetail(APIView):
    """특정 예약정보 RUD"""
    def get_object(self, pk):
        try:
            return Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """특정 예약정보 조회 /booking/{pk}"""
        queryset = self.get_object(pk)
        serializer = BookingSerializer(queryset)
        return Response(serializer.data)
