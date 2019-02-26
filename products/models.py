from django.db import models

# Create your models here.

class Product(models.Model):
    Title       = models.CharField(max_length=120)
    Description = models.TextField(blank=True, null=False)
    price       = models.DecimalField(max_digits=10000,decimal_places=2)
    summary     = models.TextField(default='This is cool!')
