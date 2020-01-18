from django.db import models
from django.contrib.auth.models import User
from ideas.models import Idea
# Create your models here.

class Join(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)

