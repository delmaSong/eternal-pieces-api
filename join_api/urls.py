from django.urls import path, include
from django.contrib import admin
from rest_framework import routers


from join_api.views import JoinViewSet
from join_api import views

router = routers.DefaultRouter()
router.register('join_api', JoinViewSet) #prefix = join_api, viewset = MovieViewSet

post_list = JoinViewSet.as_view({
    'post' : 'create',
    'get' : 'list',
})

urlpatterns = [
    path(r'',include(router.urls)),
    path('aaa/', post_list, name="post_list"),
    path('hello-view/', views.JoinApiView.as_view()),
]
