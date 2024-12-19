from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    # Maths = models.IntegerField()
    # Science = models.IntegerField()
    # English = models.IntegerField()
    city = models.CharField(max_length=50)

