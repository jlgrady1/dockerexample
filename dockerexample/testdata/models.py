from __future__ import unicode_literals

from django.db import models


class Data(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    key = models.CharField(max_length=45)
    value = models.CharField(max_length=255)
