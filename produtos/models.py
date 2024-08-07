from django.db import models

# Create your models here.

class Produto(models.Model):
  name = models.CharField(max_length=255)
  price = models.FloatField()

  created_at = models.DateTimeField(auto_now_add=True,null=True)
  updated_at = models.DateTimeField(auto_now=True,null=True)