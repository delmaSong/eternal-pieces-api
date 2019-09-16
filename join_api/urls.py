from django.urls import path, include
from django.contrib import admin
from rest_framework import routers


from join_api.views import JoinViewSet
from join_api import views

router = routers.DefaultRouter()
router.register('join_api', JoinViewSet, basename='join_api') #prefix = join_api, viewset = MovieViewSet

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path('aaab/',include(router.urls)),
    path('hello-view/', views.JoinApiView.as_view()),
]
