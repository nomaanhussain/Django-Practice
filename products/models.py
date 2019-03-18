from django.db import models
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    Title       = models.CharField(max_length=120)
    Description = models.TextField(blank=True, null=False)
    price       = models.DecimalField(max_digits=10000,decimal_places=2)
    summary     = models.TextField(default='This is cool!')

    def get_absolute_url(self):
        # return "/product/"
        return reverse("product-detail-view", kwargs={'id':self.id})