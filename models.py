from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField()
    description=models.TextField()
    image=models.ImageField()
    counter=models.IntegerField(default=1)

