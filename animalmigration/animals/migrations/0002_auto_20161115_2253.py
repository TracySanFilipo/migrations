# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 22:53
from __future__ import unicode_literals

from django.db import migrations
from django.db import models

def load_species(apps, schema_editor):
    Species = apps.get_model("animals", "Species")
    species1 = Species(id=0, scientific_name='Camelus ferus', common_name='Wild Bactrian Camel', current_population=950, historic_population=1200, historic_year=1980, percent_decline=20, native_range='AS', last_updated='2016-11-11', sci_kingdom='Animalia', sci_phylum='Chordata', sci_class='Mammalia', sci_order='Cetartiodactyla', sci_family='Camelidae', pop_trend='Decr', upper_weight=450, weight_units='kg')
    species1.save()
    species2 = Species(id=1, scientific_name='Acinonyx jubatus', common_name='Cheetah', current_population=9000, historic_population=100000, historic_year=1900, percent_decline=91, native_range='AF,AS', last_updated='2016-11-11', sci_kingdom='Animalia', sci_phylum='Chordata', sci_class='Mammalia', sci_order='Carnivora', sci_family='Felidae', pop_trend='Decr', upper_weight=72, weight_units='kg')
    species2.save()
    species3 = Species(id=2, scientific_name='Pan troglodytes', common_name='Chimpanzee', current_population=150000, historic_population=1000000, historic_year=1950, percent_decline=85, native_range='AF', last_updated='2016-11-11', sci_kingdom='Animalia', sci_phylum='Chordata', sci_class='Mammalia', sci_order='Primates', sci_family='Hominidae', pop_trend='Decr', upper_weight=65, weight_units='kg')
    species3.save()
    species4 = Species(id=3, scientific_name='Pan paniscus', common_name='Bonobo', current_population=30000, historic_population=60000, historic_year=1980, percent_decline=50, native_range='AF', last_updated='2016-11-11', sci_kingdom='Animalia', sci_phylum='Chordata', sci_class='Mammalia', sci_order='Primates', sci_family='Hominidae', pop_trend='Decr', upper_weight=60, weight_units='kg')
    species4.save()
    species5 = Species(id=4, scientific_name='Gymnogyps californianus', common_name='Calafornia Condor', current_population=435, historic_population=1000, historic_year=1900, percent_decline=56, native_range='NA', last_updated='2016-11-11', sci_kingdom='Animalia', sci_phylum='Chordata', sci_class='Aves', sci_order='Cathartiformes', sci_family='Cathartidae', pop_trend='Incr', upper_weight=12, weight_units='kg')
    species5.save()
    species6 = Species(id=5, scientific_name='Platanista gangetica', common_name='South Asian River Dolphin', current_population=1000, historic_population=5000, historic_year=1982, percent_decline=80, native_range='AS', last_updated='2016-11-11', sci_kingdom='Animalia', sci_phylum='Chordata', sci_class='Mammalia', sci_order='Cetartiodactyla', sci_family='Platanistidae', pop_trend='Unkn', upper_weight=89, weight_units='kg')
    species6.save()
    species7 = Species(id=6, scientific_name='Elephas maximus', common_name='Asian Elephant', current_population=40000, historic_population=100000, historic_year=1900, percent_decline=40, native_range='AS', last_updated='2016-11-11', sci_kingdom='Animalia', sci_phylum='Chordata', sci_class='Mammalia', sci_order='Proboscidea', sci_family='Elephantidae', pop_trend='Decr', upper_weight=7000, weight_units='kg')
    species7.save()
    species8 = Species(id=7, scientific_name='Loxodonta africana', common_name='African Elephant', current_population=470000, historic_population=2000000, historic_year=1900, percent_decline=76, native_range='AF', last_updated='2016-11-11', sci_kingdom='Animalia', sci_phylum='Chordata', sci_class='Mammalia', sci_order='Proboscidea', sci_family='Elephantidae', pop_trend='Incr', upper_weight=7000, weight_units='kg')
    species8.save()
    species9 = Species(id=8, scientific_name='Ursus maritimus', common_name='Polar Bear', current_population=20000, historic_population=25000, historic_year=1990, percent_decline=5, native_range='NA,EU', last_updated='2016-11-11', sci_kingdom='Animalia', sci_phylum='Chordata', sci_class='Mammalia', sci_order='Carnivora', sci_family='Ursidae', pop_trend='Unkn', upper_weight=700, weight_units='kg')
    species9.save()
    species10 = Species(id=9, scientific_name='Bison bison', common_name='American Bison', current_population=30000, historic_population=60000000, historic_year=1700, percent_decline=99, native_range='NA', last_updated='2016-11-11', sci_kingdom='Animalia', sci_phylum='Chordata', sci_class='Mammalia', sci_order='Cetartiodactyla', sci_family='Bovidae', pop_trend='Stab', upper_weight=1000, weight_units='kg')
    species10.save()
    species11 = Species(id=10, scientific_name='Panthera uncia', common_name='Snow Leopard', current_population=5000, historic_population=7500, historic_year=2000, percent_decline=33, native_range='AS,EU', last_updated='2016-11-11', sci_kingdom='Animalia', sci_phylum='Chordata', sci_class='Mammalia', sci_order='Carnivora', sci_family='Felidae', pop_trend='Decr', upper_weight=55, weight_units='kg')
    species11.save()

class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
    migrations.RunPython(load_species)
    ]
