from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)


    # Additional Fields
    address = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    userimg = models.ImageField(upload_to='userimg/',blank=True,null=True)