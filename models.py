from django.db import models


class golf_platform(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='clothes/')
    brand = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

# Create your models here.
