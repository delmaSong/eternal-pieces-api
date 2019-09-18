from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=30, unique=True, primary_key=True)
    user_pw = models.CharField(max_length=30)
    role_tatt = models.BooleanField(default=False)  #기본값 no tattist

    def __str__(self):
        return self.user_id
    
