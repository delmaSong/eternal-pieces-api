from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from login_api.views import UserLoginViewSet

router = routers.DefaultRouter()
router.register('login_api', UserLoginViewSet)

urlpatterns =[
    url(r'', include(router.urls)),
]
