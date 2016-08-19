from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
	name = models.CharField(max_length=250)
	street = models.CharField(max_length=250)
	city = models.CharField(max_length=250)
	state = models.CharField(max_length=250)
	zipcode = models.IntegerField() 
	diagnosis_related_group = models.CharField(max_length=250)
	avg_covered_charges = models.FloatField()
	avg_total_payments = models.FloatField()
	avg_medicare_payments= models.FloatField()

	def __str__(self):
		return self.name
		
class ZipCode(models.Model):
    zipcode = models.CharField(max_length=10)
    statecode = models.CharField(max_length=2)
    latitude = models.FloatField()
    longitude = models.FloatField()
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=32)

    def __unicode__(self):
        return "%s, %s (%s)" % (self.zipcode, self.statecode, self.city) 

    class Meta:
        ordering = ['zipcode']