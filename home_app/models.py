from django.db import models


# Create your models here.
class Recruiter(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    email_id = models.EmailField()
    phone_number = models.IntegerField()
