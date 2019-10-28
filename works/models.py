from django.db import models
from login_api.models import User

# Create your models here.
class Works(models.Model):
    tatt_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column = 'tatt_id')
    works = models.ImageField(upload_to="works")
