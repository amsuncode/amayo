from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

#Q-bank segment

class Papers(models.Model):
    question_id = models.CharField(max_length=100)
    question_text = models.TextField()
    options = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    year_of_study = models.IntegerField()
    unit = models.CharField(max_length=100)
    question_type = models.CharField(max_length=100)
