# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cereal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('cer_type', models.CharField(max_length=255, null=True, blank=True)),
                ('calories', models.IntegerField(null=True, blank=True)),
                ('protein', models.IntegerField(null=True, blank=True)),
                ('fat', models.IntegerField(null=True, blank=True)),
                ('sodium', models.IntegerField(null=True, blank=True)),
                ('fiber', models.FloatField(null=True, blank=True)),
                ('carbs', models.FloatField(null=True, blank=True)),
                ('sugars', models.IntegerField(null=True, blank=True)),
                ('potassium', models.IntegerField(null=True, blank=True)),
                ('vits_mins', models.IntegerField(null=True, blank=True)),
                ('ss_weight', models.FloatField(null=True, blank=True)),
                ('cups_per_s', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='cereal',
            name='manuf',
            field=models.ForeignKey(blank=True, to='main.Manufacturer', null=True),
        ),
    ]
