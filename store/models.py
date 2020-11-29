from django.db import models

# Create your models here.
class Med(models.Model):
    Medicine_batch_no = models.IntegerField()
    Medicine_name = models.CharField(null=True,max_length=50)
    Medicine_Company = models.CharField(null=True,max_length=50)
    Medical_quantity = models.IntegerField()
    med_purchase_date = models.DateField()
    Med_type = models.CharField(null=True,max_length=50)
    Med_price = models.IntegerField()