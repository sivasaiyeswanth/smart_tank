import profile
from pyexpat import model
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


class TankData(models.Model):
    current_level = models.IntegerField()  # e.g., 0 to 100
    threshold = models.IntegerField(default=50)  # User-defined threshold
    pump_status = models.BooleanField(default=False)  # On or Off
    last_updated = models.DateTimeField(auto_now_add=True)