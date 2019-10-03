from django.urls import path, include
from design import views
urlpatterns = [
    path(r'',views.DesignCreate.as_view(), name='DesignList' ),
    path(r'<str:pk>/', views.DesignDetail.as_view(), name='detail'),
]
