from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class User(models.Model):
    username = models.CharField(max_length=191)
    email = models.EmailField(unique=True, max_length=191)
    password = models.CharField(max_length=191)
    accountType = models.CharField(max_length=191)
    userID = models.CharField(max_length=191)

    class Meta:
        db_table = 'userB'