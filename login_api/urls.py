# from django.conf.urls import url, include
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
# from login_api.views import UserLoginViewSet
from login_api import views
from login_api.views import LoginViewSet
# from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()
# router.register('login_api', LoginList)

# urlpatterns =[
#     # url(r'', include(router.urls)),
#     url(r'', views.LoginList.as_view()),
#     url(r'<String:pk>/', views.UserDetail.as_view())
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)


router = routers.DefaultRouter()
router.register('login_api', LoginViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
