from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from django.http import Http404

from login_api.serializers import UserLoginSerializer
from login_api.models import User

# # Create your views here.
# class UserLoginViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserLoginSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def perform_create(self, serializer):
        serializer.save()

    def post(user_id, user_pw, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            id = serializer.validated_data.get('user_id')
            message = f'Good works with {id}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.error,
                status=status.HTTP_400_BAD_REQUEST
            )







# class LoginList(APIView):
#
#     def get(self, request, format=None):        #read
#         user = User.objects.all()
#         serializer = UserLoginSerializer(user, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):       #create
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
#
# class UserDetail(APIView):
#     """유저 테이블 조회, 업데이트, 삭제"""
#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserLoginSerializer(user)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserLoginSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
#
#     def delete(self, reqeust, pk, format=None):
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
