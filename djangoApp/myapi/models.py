from django.db import models

# Create your models here.
class Countries(models.Model):
  country_name=models.CharField(max_length=60)
  capital=models.CharField(max_length=60)
  population=models.FloatField()
  
  def __str__(self):
    return self.country_name