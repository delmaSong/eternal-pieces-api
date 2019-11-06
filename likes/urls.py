from django.urls import path, include
from likes import views

urlpatterns = [
    path(r'',views.LikesCreate.as_view()),
    path(r'<str:pk>/', views.LikesDetail.as_view()),
]
