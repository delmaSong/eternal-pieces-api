from django.db import models
from join_api.models import Join_tattist
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Design(models.Model):
    design_name = models.CharField(max_length=500) #도안 이름
    design_photho = models.ImageField(upload_to="designs")
    design_price = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    design_size = models.IntegerField(default=0)
    design_spent_time = models.IntegerField(default=0)
    design_style = models.CharField(max_length=200)
    design_desc = models.CharField(max_length=1000)
    tatt_id = models.ForeignKey(Join_tattist, on_delete=models.CASCADE, db_column = 'tatt_id')
