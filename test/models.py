#!/bin/python3
from django.db import models

# Sample User model
class User(models.Model):
    name = models.CharField(max_length=50, default="")
