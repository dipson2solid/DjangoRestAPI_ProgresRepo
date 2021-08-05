from django.db import models

# Create your models here.

class Customers(models.Model):
    CustomerId = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=500)

