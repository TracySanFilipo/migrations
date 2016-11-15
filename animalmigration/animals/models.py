from django.db import models

# Create your models here.
class Species(models.Model):
    scientific_name = models.CharField(max_length=40)
    common_name  = models.CharField(max_length=25)
    current_population = models.IntegerField(default=0)
    historic_population = models.IntegerField(default=0)
    historic_year = models.IntegerField(default=0)
    percent_decline = models.DecimalField(max_digits=5, decimal_places=2)
    native_range = models.CharField(max_length=5)
    last_updated = models.DateTimeField("date")
    sci_kingdom = models.CharField(max_length=30)
    sci_phylum = models.CharField(max_length=30)
    sci_class = models.CharField(max_length=30)
    sci_order = models.CharField(max_length=30)
    sci_family = models.CharField(max_length=30)
    pop_trend = models.CharField(max_length=4)
    upper_weight = models.IntegerField(default=0)
    weight_units = models.CharField(max_length=12)
