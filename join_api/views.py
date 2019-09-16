from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import JoinSerializer
from .models import Join_tattist

# Create your views here.
class JoinViewSet(viewsets.ModelViewSet):
    qeuryset = Join_tattist.objects.all()
    serializer_class = JoinSerializer

class JoinApiView(APIView):

    def get(self, request, format=None):
        an_apiview =[
            'this',
            'is',
            'an apiview',
        ]

        return Response({'message' : 'Hello!', 'an_apiview' : an_apiview})
