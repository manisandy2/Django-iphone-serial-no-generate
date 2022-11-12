from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Generate_Serial(models.Model):
    mpn = models.CharField(max_length=25, unique=False)
    ingram_code = models.CharField(max_length=50, unique=False)
    item_code = models.CharField(max_length=10, unique=False)
    apx_model = models.CharField(max_length=500, unique=False)
    brand = models.CharField(max_length=15, unique=False)
    product = models.CharField(max_length=30, unique=False)

    def __str__(self):
        return self.apx_model

    class Meta:
        db_table = 'generate'


class Product_List(models.Model):
    list_of_category = [
        ("mpn", "MPN"),
        ("ingram_code", "INGRAM CODE"),
        ("item_code", "ITEM CODE"),
    ]
    name = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True)
    serial = models.CharField(max_length=25)
    list_of_range = models.PositiveIntegerField(null=True)
    list_of_name = models.CharField(max_length=25,choices=list_of_category,unique=False,null=True)
    list_of_code = models.CharField(max_length=25,unique=False,null=True)
    list_of_itemcode = models.CharField(max_length=25, unique=False, null=True)
    name_invoice_create = models.CharField(max_length=250,unique=False)
    invoice = models.CharField(max_length=250,unique=False)