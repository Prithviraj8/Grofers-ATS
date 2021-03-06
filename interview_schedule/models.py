from django.db import models


# Create your models here.
class interviewer(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(default='')
    name = models.CharField(max_length=100)
