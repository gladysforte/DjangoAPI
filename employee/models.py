from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=300, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)