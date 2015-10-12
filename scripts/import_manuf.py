import csv
import sys
import os

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import Manufacturer

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "cereal.csv"

cereal_csv = os.path.join(dir_name, file_name)

csv_file = open(cereal_csv, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
    new_name, created = Manufacturer.objects.get_or_create(name=row['Manufacturer'])

    new_name.save()
