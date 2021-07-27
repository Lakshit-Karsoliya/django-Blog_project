from django.db import models
from datetime import datetime
# Create your models here.
class blog(models.Model):
    heading=models.CharField(max_length=50)
    content=models.CharField(max_length=10000)
    created_at = models.DateTimeField(default=datetime.now,blank=True)