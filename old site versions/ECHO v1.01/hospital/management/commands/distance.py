from hospital.models import Item, ZipCode
from math import *
import django
import os, sys
from django.core.management.base import BaseCommand

django.setup()
os.environ['DJANGO_SETTINGS_MODULE'] = '..website.settings'


class Command(BaseCommand):
	help = "Find distance between zipcodes"
	def add_arguments(self, parser):
		parser.add_argument('zipcode_1')
		parser.add_argument('zipcode_2')

	def handle(self, *args, **options):
		zipcodes = ZipCode.objects.all()
		zipcode_1 = options['zipcode_1']
		zipcode_2 = options['zipcode_2']
		distance = self.calcDist(zipcodes.get(zipcode=zipcode_1), zipcodes.get(zipcode=zipcode_2))
		print(distance)

	def calcDist(self, zipcode_1, zipcode_2):
		lat_A 	= zipcode_1.latitude
		long_A 	= zipcode_1.longitude
		lat_B 	= zipcode_2.latitude
		long_B 	= zipcode_2.longitude

		distance = (sin(radians(lat_A)) * sin(radians(lat_B)) + cos(radians(lat_A)) * cos(radians(lat_B)) * cos(radians(long_A - long_B)))
		distance = (degrees(acos(distance))) * 69.09

		return distance
