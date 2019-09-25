from django.db import models
from login_api.models import User

# Create your models here.
class Join_tattist(models.Model):
    tatt_work = models.CharField(max_length=1000, blank=True, null=True)    # 시술사진. Application단 null OK, DB단 null OK
    tatt_addr = models.CharField(max_length=200)    #타티스트 주소
    tatt_intro = models.CharField(max_length=200)   #타티스트 간단 소개
    tatt_time = models.CharField(max_length=200)    #타티스트 작업 가능 시간
    tatt_date = models.CharField(max_length=200)    #타티스트 작업 가능 요일
    tatt_profile = models.ImageField(upload_to="") #타티스트 프로필 사진
    tatt_id = models.ForeignKey(User ,on_delete=models.CASCADE, db_column = 'tatt_id')       #타티스트 아이디

    # def __str__(self):
    #     return self.tatt_id
