from django.db import models


class user(models.Model):
    userId = models.AutoField(primary_key=True)
    user = models.CharField(max_length=50 , null=True)
    password = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=100 , null=True)
    firstName = models.CharField(max_length=100 , null=True)
    lastName = models.CharField(max_length=100, null=True)
    isAdmin = models.BooleanField(default=False)