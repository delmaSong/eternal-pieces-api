from django.urls import path, include
from join_api import views


urlpatterns = [
    path(r'', views.JoinList.as_view(), name='JoinList'),
    path(r'<str:pk>/', views.UserDetail.as_view()),
]
