from django.db import models
from django.conf import settings
from ideas.models import Idea
# Create your models here.

class Join(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)

    def __str__(self):
        return "'{}' 님이 '{}' 아이디어를 스크랩 함".format(self.user, self.idea)
