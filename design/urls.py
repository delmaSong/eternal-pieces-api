from django.urls import path, include
from design import views

urlpatterns = [
    path(r'upload-design/',views.DesignList.as_view(), name='DesignList' ),
]
