from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Cereal(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    manuf = models.ForeignKey(Manufacturer, null=True, blank=True)
    cer_type = models.CharField(max_length=255, null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True)
    protein = models.IntegerField(null=True, blank=True)
    fat = models.IntegerField(null=True, blank=True)
    sodium = models.IntegerField(null=True, blank=True)
    fiber = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    sugars = models.IntegerField(null=True, blank=True)
    potassium = models.IntegerField(null=True, blank=True)
    vits_mins = models.IntegerField(null=True, blank=True)
    ss_weight = models.FloatField(null=True, blank=True)
    cups_per_s = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return self.name
