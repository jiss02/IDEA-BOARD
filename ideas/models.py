from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Idea(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    detail = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)