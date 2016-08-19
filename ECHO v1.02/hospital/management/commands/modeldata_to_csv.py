from hospital.models import Item
import csv
import django
import os, sys
from django.core.management.base import BaseCommand

django.setup()
os.environ['DJANGO_SETTINGS_MODULE'] = '..website.settings'


class Command(BaseCommand):
    help = "output hospitals to .csv"

    def handle(self, *args, **options):

        field_names = [f.name for f in Item._meta.fields]
        writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
        writer.writerow(field_names)
        for instance in Item.objects.all():
            writer.writerow([str(getattr(instance, f)).encode('utf-8') for f in field_names])