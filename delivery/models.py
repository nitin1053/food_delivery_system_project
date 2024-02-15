# models.py

from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    type = models.CharField(max_length=50)
    description = models.TextField()

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=50)
    base_distance_in_km = models.PositiveIntegerField()
    km_price = models.DecimalField(max_digits=5, decimal_places=2)
    fixed_price = models.DecimalField(max_digits=10, decimal_places=2)
