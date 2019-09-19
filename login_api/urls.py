from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
# from login_api.views import UserLoginViewSet
from login_api import views
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()
# router.register('login_api', LoginList)

urlpatterns =[
    # url(r'', include(router.urls)),
    url(r'', views.LoginList.as_view()),
    url(r'(?P<pk>[0-9]+)/$', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
