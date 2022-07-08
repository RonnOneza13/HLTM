from django.db import models


class HealthyContact(models.Model):
	LName = models.CharField(blank = True, max_length=100)
	Fname = models.CharField(blank = True, max_length=100)
	PAddress = models.CharField(blank = True, max_length=100)
	Pnumber = models.IntegerField(blank = True)
	Food = models.CharField(blank = True, max_length=100)
	Order = models.CharField(blank = True, max_length=100)

class ModPayDate(models.Model):
	DToday = models.DateField(blank = True, max_length=100)
	DelToday = models.DateField(blank = True, max_length=100)
	Mop = models.CharField(blank = True, max_length=100)