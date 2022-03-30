from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

UserModel = get_user_model()
class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    born = models.DateField()
    phone = models.CharField(max_length=13, validators=(
        RegexValidator(r'^\+380[\d]{9}$', 'Invalid phone number. Example: +380xxxxxxxxx'),
    ))
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
