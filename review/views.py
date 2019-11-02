from django.http import Http404
from rest_framework import status, permissions
from rest_framework import mixins, generics
from rest_framework.response import Response

from .serializers import ReviewSerializer
from .models import Review

class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
