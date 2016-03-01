from __future__ import unicode_literals

from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name


