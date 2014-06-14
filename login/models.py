from django.db import models

# Create your models here.
class AppUser(models.Model):
    name = models.CharField(unique=True, max_length=100)
    password = models.CharField(blank=False, max_length=64)
    salt = models.CharField(blank=False, max_length=16)
    plan = models.IntegerField(blank=False, null=False)
    email = models.EmailField(primary_key = True, max_length=200)
