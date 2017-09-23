# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length = 32, unique = True)
    days = models.IntegerField(default = 0)
    charges = models.DecimalField(max_digits=6, decimal_places=5)
    def __str__(self):
        return self.name

class record(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    category = models.ForeignKey(categories)
    interest = models.DecimalField(max_digits=6, decimal_places=5)
    fund = models.IntegerField(default = 0)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return '%s ---- %s --- %d --- %.3f' % (self.start_date, self.end_date, self.fund, self.interest)
