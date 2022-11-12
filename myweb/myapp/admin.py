from django.contrib import admin
from .models import Generate_Serial,Product_List
from  import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Generate_Serial)
class Admin_Generate_Serial(ImportExportModelAdmin):
    fields = ['mpn', 'ingram_code', 'item_code', 'apx_model', 'brand', 'product']


@admin.register(Product_List)
class Admin_Product_List(admin.ModelAdmin):
    fields = ['name', 'list_of_code', 'serial', 'list_of_range']
    list_display = ['name', 'date', 'serial', 'list_of_name', 'list_of_code', 'list_of_range', 'name_invoice_create', 'invoice']

