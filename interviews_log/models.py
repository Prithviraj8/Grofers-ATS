from django.db import models


# Create your models here.
class interview(models.Model):
    id = models.IntegerField(primary_key=True)
    interviewer_email = models.EmailField(default='')
    interviewer_name = models.CharField(max_length=100)
    candidate_email = models.EmailField(default='')
    candidate_name = models.CharField(max_length=100)
