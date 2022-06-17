from django.db import models

# Create your models here.
"""
-------------
Name | price
-------------
"""

class MobileDeviceModel(models.Model):

	mobile_name = models.CharField(max_length=100)
	mobile_price = models.FloatField()
	mobile_quantity = models.PositiveIntegerField()


