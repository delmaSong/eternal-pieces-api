from django.db import models
from design.models import Design
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Booking(models.Model):
    booker = models.CharField(max_length=100) #예약자 아이디
    book_date = models.CharField(max_length=100) #시술 날짜
    book_time = models.CharField(max_length=20) #시술 시간
    book_price = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(300)]) #예약 가격. 최대 300만원
    book_part = models.CharField(max_length=50) #시술 부위
    book_size = models.CharField(max_length=50) #시술 받을 도안 크기
    book_comm = models.CharField(max_length=500)    #예약자 코멘트
    #예약할 도안 사진. 도안 테이블에서 url 주소만 가져와 저장하도록 하기
    book_photo = models.CharField(max_length=500)
    book_tatt = models.CharField(max_length=100)    #tattist id
    design_id = models.ForeignKey(Design, on_delete=models.CASCADE, db_column='design_id')
