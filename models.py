from django.db import models
from datetime import datetime
class sales(models.Model):
    CreatedAt=models.DateField(default=datetime.now)
    Name=models.CharField(max_length=255)
    Weight=models.CharField(max_length=255)
    Price=models.CharField(max_length=255)


