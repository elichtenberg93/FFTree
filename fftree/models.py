from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Brother(models.Model):
	name = models.CharField(max_length=200)
	grad_year = models.IntegerField(default=0)
	init_year = models.IntegerField(default=0)
	# add bigbrother id list field
	# add littlebrother id list field
	# add fields for images? links? etc.

	def __str__(self):
		return self.name