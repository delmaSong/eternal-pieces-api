from django.urls import path, include
from works import views

urlpatterns = [
    path(r'',views.WorksCreate.as_view() ),
]
