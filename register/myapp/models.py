from django.db import models
from django.contrib.auth.admin import User

# Create your models here.
class ProfileInfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    Portfolio_site=models.URLField(blank=True)
    Profile_pic=models.ImageField(upload_to='profile_pic',blank=True)


    def __str__(self):
        return self.user.username