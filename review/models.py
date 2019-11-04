from django.db import models
from join_api.models import Join_tattist
from design.models import Design

#review table
class Review(models.Model):
    rv_writer = models.CharField(max_length=100)    #작성자
    rv_title = models.CharField(max_length=50)      #제목
    rv_contents = models.CharField(max_length=500)  #내용
    rv_date = models.DateField(auto_now=True)   #작성시간
    rv_photo = models.ImageField(upload_to="review", null=True)    #리뷰 이미지
    rv_rate = models.CharField(max_length=10)   #별점
    rv_tatt = models.ForeignKey(Join_tattist, on_delete=models.CASCADE, db_column='rv_tatt')#리뷰 대상 타티스트
    rv_design = models.ForeignKey(Design, on_delete=models.CASCADE, db_column='rv_design')#리뷰 대상 도안
