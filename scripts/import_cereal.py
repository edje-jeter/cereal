import csv
import sys
import os

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import Manufacturer, Cereal

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "cereal.csv"

cereal_csv = os.path.join(dir_name, file_name)

csv_file = open(cereal_csv, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
    new_cereal, created = Cereal.objects.get_or_create(name=row['Cereal Name'])
    # new_cereal.manuf = row['Manufacturer']
    new_cereal.cer_type = row['Type']
    new_cereal.calories = row['Calories']
    new_cereal.protein = row['Protein (g)']
    new_cereal.fat = row['Fat']
    new_cereal.sodium = row['Sodium']
    new_cereal.fiber = row['Dietary Fiber']
    new_cereal.carbs = row['Carbs']
    new_cereal.sugars = row['Sugars']
    new_cereal.potassium = row['Potassium']
    new_cereal.vits_mins = row['Vitamins and Minerals']
    new_cereal.ss_weight = row['Serving Size Weight']
    new_cereal.cups_per_s = row['Cups per Serving']

    try:
        new_manuf = Manufacturer.objects.get(name=row['Manufacturer'])
        new_cereal.manuf = new_manuf
    except Exception, e:
        new_cereal.manuf = None

    new_cereal.save()
