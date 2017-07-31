from __future__ import unicode_literals

from django.db import models
from EmployeeManagemnt.settings import BASE_DIR


class Vendor(models.Model):
	name = models.CharField(max_length=50, unique=True)
	tin = models.IntegerField()
	location = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Inventory(models.Model):
	item_name = models.CharField(max_length=100, unique=True)
	item_id = models.IntegerField()
	description =  models.CharField(max_length=200)
	vendor_name = models.ForeignKey(Vendor)
	photo =  models.ImageField(upload_to='{0}\MyApp\static\images'.format(BASE_DIR), max_length=100)
	is_active = models.CharField(max_length=10, default='True')

	def __unicode__(self):
		return self.item_name

