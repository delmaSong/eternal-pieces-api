from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import JoinSerializer
from .models import Join_tattist

# Create your views here.
class JoinViewSet(viewsets.ModelViewSet):
    queryset = Join_tattist.objects.all()
    serializer_class = JoinSerializer

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request):
        serializer = self.serializer_class(data=requeset.data)

        if serializer.is_valid():
            id = serializer.validated_data.get('tatt_id')
            message = f'Good works with {id}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.error,
                status=status.HTTP_400_BAD_REQUEST
            )

class JoinApiView(APIView):

    def get(self, request, format=None):
        an_apiview =[
            'this',
            'is',
            'an apiview',
        ]

        return Response({'message' : 'Hello!', 'an_apiview' : an_apiview})
