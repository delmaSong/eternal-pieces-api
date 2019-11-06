from django.db import models

class Likes(models.Model):
    user = models.CharField(max_length=50) #현재 로그인한 사용자
    like_design = models.CharField(max_length=10, null=True) #좋아하는 도안
    like_tattist = models.CharField(max_length=10, null=True) #좋아하는 타티스트 
