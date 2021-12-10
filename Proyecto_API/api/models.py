from django.db import models
from django.db.models.fields import CharField, PositiveIntegerField, URLField

class Company(models.Model):
    name = CharField(max_length=50)
    website = URLField(max_length=100)
    foundation = PositiveIntegerField()