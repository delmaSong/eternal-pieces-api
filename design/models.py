from django.db import models
from login_api.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Design(models.Model):
    design_name = models.CharField(max_length=500) #도안 이름
    design_price = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    design_size = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    design_spent_time = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    design_style = models.CharField(max_length=200)
    design_desc = models.CharField(max_length=1000)
    tatt_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column = 'tatt_id')
    design_photo = models.ImageField(upload_to="designs")
