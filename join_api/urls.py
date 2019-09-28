from django.urls import path, include
from join_api import views


urlpatterns = [
    path(r'join_api/', views.JoinList.as_view(), name='JoinList'),
]
