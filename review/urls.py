from django.urls import path, include
from review import views


urlpatterns = [
    path(r'', views.ReviewList.as_view()),
    path(r'<str:pk>/', views.ReviewDetail.as_view()),
]
